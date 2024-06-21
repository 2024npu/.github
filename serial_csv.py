import serial
import csv
import time

def read_serial_data(serial_port, baud_rate, output_csv):
    # Open the serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    
    # Open the CSV file for writing
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write a header row to the CSV file (modify according to your data structure)
        csvwriter.writerow(['Timestamp', 'Data'])
        
        try:
            while True:
                if ser.in_waiting > 0:
                    # Read a line from the serial port
                    line = ser.readline().decode('utf-8').strip()
                    
                    # Write the timestamp and data to the CSV file
                    csvwriter.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), line])
                    
                    # Print the data (optional)
                    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {line}")
        
        except KeyboardInterrupt:
            print("Terminating...")
        
        finally:
            # Close the serial port
            ser.close()

# Example usage
if __name__ == "__main__":
    serial_port = '/dev/ttyUSB0'  # Replace with your serial port
    baud_rate = 9600  # Replace with your baud rate
    output_csv = 'output.csv'
    
    read_serial_data(serial_port, baud_rate, output_csv)
