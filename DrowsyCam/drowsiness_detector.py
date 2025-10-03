import cv2
import mediapipe as mp
import math
from playsound import playsound
import threading

# === Constants ===
EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 20
NO_FACE_LIMIT = 50  # frames without face before triggering absence action

# === State Variables ===
frame_counter = 0
no_face_counter = 0
drowsy_alerted = False

# === Initialize MediaPipe Face Mesh ===
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
drawing_utils = mp.solutions.drawing_utils

# === Eye Landmark Indices (MediaPipe) ===
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# === Calculate Eye Aspect Ratio ===
def calculate_ear(eye_indices, landmarks):
    def distance(a, b):
        return math.hypot(
            landmarks[a].x - landmarks[b].x,
            landmarks[a].y - landmarks[b].y
        )
    A = distance(eye_indices[1], eye_indices[5])
    B = distance(eye_indices[2], eye_indices[4])
    C = distance(eye_indices[0], eye_indices[3])
    ear = (A + B) / (2.0 * C)
    return ear

# === Alert Sound ===
def play_alert():
    playsound("alert.wav")

# === Start Webcam ===
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        no_face_counter = 0
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark
            left_ear = calculate_ear(LEFT_EYE, landmarks)
            right_ear = calculate_ear(RIGHT_EYE, landmarks)
            avg_ear = (left_ear + right_ear) / 2.0

            # Drowsiness detection
            if avg_ear < EAR_THRESHOLD:
                frame_counter += 1
                if frame_counter >= CONSEC_FRAMES and not drowsy_alerted:
                    print("Drowsiness detected!")
                    threading.Thread(target=play_alert).start()
                    drowsy_alerted = True
            else:
                frame_counter = 0
                drowsy_alerted = False

            # Annotate EAR
            cv2.putText(frame, f'EAR: {avg_ear:.2f}', (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 0) if avg_ear >= EAR_THRESHOLD else (0, 0, 255), 2)
    else:
        no_face_counter += 1
        if no_face_counter > NO_FACE_LIMIT:
            print("User not detected. You may want to lock screen or log event.")
            no_face_counter = 0  # Reset if you want one-time action

    # Show the frame
    cv2.imshow("Drowsiness & Presence Monitor", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
