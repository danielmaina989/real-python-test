# Front-end, Back-end, and Middleware
# 1. Front-end: The presentation layer. It's what the end user sees when interacting with
# ...a web application
# . HTML defines the structure, while CSS provides a pretty facade,
# ...and JavaScript provides user interaction.
# 2. Middleware: This layer relays information between the front and back-end, in order
# ...to: Process HTTP requests and responses;Connect to the server;Interact with APIs;Manage URL routing, authentication, sessions, and cookies.
# 3. Back-end: This is where data is stored, analyzed, and processed. Languages such
# ...as Python, PHP, and Ruby communicate back and forth with the database, web
# ...service, or other data source to produce the end-user’s requested data

# Model-View-Controller (MVC)
# Web frameworks reside just above those three layers
# Web frameworks simplify web development, by handling much of the superfluous, repetitious tasks.
# Frameworks also separate the presentation (view) from the application logic (controller)
# ...and the underlying data (model) in what’s commonly referred to as the Model-View-Controller-architecture pattern.
# While the front-end, back-end, and middleware layers operate linearly, MVC generally operates in a triangular pattern:
# front-end view --->middleware logic --> backend Data while mvc is triangle <--> view 	<--> controller <--> model.
# The difference between static websites and dynamic websites is that static websites appear the same for every user
# ... that accesses them and only change when a developer modifies the source files, whereas dynamic websites can present different information to different visitors.