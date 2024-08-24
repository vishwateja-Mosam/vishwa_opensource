import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.List;

public class TravelAndTourism extends JFrame {
    // List to store bookings
    private List<Booking> bookingsList;

    // GUI components
    private JTextField tfDestination, tfDate, tfNumberOfPeople;
    private JButton btnBookTour, btnViewTours;

    // Inner class to represent a booking
    private class Booking {
        String destination;
        String date;
        int numberOfPeople;

        Booking(String dest, String date, int numPeople) {
            this.destination = dest;
            this.date = date;
            this.numberOfPeople = numPeople;
        }
    }

    // Constructor to setup the GUI components and event handlers
    public TravelAndTourism() {
        // Initialize the bookings list
        bookingsList = new ArrayList<>();

        // Initialize components
        tfDestination = new JTextField(20);
        tfDate = new JTextField(20);
        tfNumberOfPeople = new JTextField(20);
        btnBookTour = new JButton("Book Tour");
        btnViewTours = new JButton("View Tours");

        // Layout
        setLayout(new FlowLayout());
        add(new JLabel("Destination:"));
        add(tfDestination);
        add(new JLabel("Date (YYYY-MM-DD):"));
        add(tfDate);
        add(new JLabel("Number of People:"));
        add(tfNumberOfPeople);
        add(btnBookTour);
        add(btnViewTours);

        // Action Listeners
        btnBookTour.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                bookTour();
            }
        });

        btnViewTours.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                viewTours();
            }
        });

        // Frame settings
        setTitle("Travel and Tourism Management System");
        setSize(300, 200);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    // Method to book a tour
    private void bookTour() {
        String destination = tfDestination.getText();
        String date = tfDate.getText();
        int numberOfPeople;
        try {
            numberOfPeople = Integer.parseInt(tfNumberOfPeople.getText());
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Please enter a valid number of people.");
            return;
        }

        // Create a new booking and add it to the list
        Booking newBooking = new Booking(destination, date, numberOfPeople);
        bookingsList.add(newBooking);
        JOptionPane.showMessageDialog(null, "Tour booked successfully!");
    }

    // Method to view booked tours
    private void viewTours() {
        StringBuilder sb = new StringBuilder();
        for (Booking booking : bookingsList) {
            sb.append("Destination: ").append(booking.destination)
              .append(", Date: ").append(booking.date)
              .append(", Number of People: ").append(booking.numberOfPeople)
              .append("\n");
        }
        JOptionPane.showMessageDialog(null, sb.toString());
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new TravelAndTourism();
            }
        });
    }
}
