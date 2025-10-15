Digital Clock

A web-based digital clock application built using HTML, CSS, and JavaScript, featuring a real-time clock, alarm, timer, stopwatch, and mood selection interface.

Live demo: https://prachichoudhary2004.github.io/DigitalClock/


Features

Real-time Clock — Displays current time in hours : minutes : seconds.

Alarm — Set an alarm (HH:MM) to get a notification at the chosen time.

Timer — Simple countdown timer you can start, stop, reset.

Stopwatch — A standard stopwatch with start, pause, reset.

Mood Selector — Choose how you’re feeling (“Happy”, “Neutral”, “Sad”) via UI.

Audio Notification — Plays an audio (e.g. audio.mp3) when the alarm triggers.

Folder Structure
/
├── index.html
├── styles.css
├── script.js
├── audio.mp3
└── README.md


index.html — The HTML markup and UI layout.

styles.css — Styling for layout, theme, responsiveness.

script.js — JavaScript logic for clock, alarm, timer, stopwatch, mood UI.

audio.mp3 — Audio file used for alarm notification.

Usage

Clone or download the repo:

git clone https://github.com/prachichoudhary2004/DigitalClock.git


Open index.html in a web browser.

Use the interface to:

View the real-time clock.

Set an alarm by entering hours and minutes, then triggering “Set Alarm”.

Use the timer: input duration (or use default), then start, stop or reset.

Use the stopwatch: start, stop, and reset the count.

Select mood (Happy / Neutral / Sad) — this is for UI/UX feedback.

When alarm time is reached, the audio will play (if allowed) and visual feedback will appear.

Technologies Used

HTML5

CSS3

JavaScript (vanilla)

Browser Web APIs (e.g. setInterval, Date, audio playback)

How It Works (Brief Overview)

The real-time clock uses setInterval with Date() to update every second.

The alarm checks each minute (or each second) whether the current time matches the set alarm time, then triggers audio.

The timer is implemented with countdown logic, updating display every second until zero.

The stopwatch counts up in intervals, pausing/resuming as requested.

Mood selection is a simple UI state change (e.g. adding a CSS class) for visual feedback.


