#TRAVEL AND TOURISM
This Java code is for a simple Travel and Tourism Management System with a graphical user interface (GUI) using Swing. Here's a brief description of what the code does:

1. **Class Structure:**
   - The main class, `TravelAndTourism`, extends `JFrame` to create a window-based application.
   - An inner class `Booking` is defined to represent a booking, with fields for the destination, date, and number of people.

2. **GUI Components:**
   - The GUI includes text fields for entering the destination, date, and number of people (`tfDestination`, `tfDate`, `tfNumberOfPeople`).
   - There are two buttons: `btnBookTour` for booking a tour and `btnViewTours` for viewing all booked tours.

3. **Main Functionality:**
   - **Booking a Tour:** 
     - The `bookTour()` method is triggered when the "Book Tour" button is clicked. It reads the input values from the text fields, creates a `Booking` object, and adds it to the `bookingsList`.
     - If the number of people is not a valid integer, it shows an error message.
     - On successful booking, a confirmation message is displayed.
   - **Viewing Tours:**
     - The `viewTours()` method is triggered when the "View Tours" button is clicked. It displays all the bookings stored in `bookingsList` in a message dialog.

4. **GUI Layout and Setup:**
   - The layout is a simple `FlowLayout` that arranges the components in a single row.
   - The `JFrame` is set up with a title, size, and default close operation. The frame is centered on the screen and made visible when the application starts.

5. **Execution:**
   - The `main()` method launches the application by invoking the `TravelAndTourism` class in the Event Dispatch Thread using `SwingUtilities.invokeLater`.

In summary, this code allows users to book tours by specifying a destination, date, and number of people, and view all the bookings they have made. The data is stored in memory and displayed through message dialogs.
