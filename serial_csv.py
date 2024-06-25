import serial
import pickle

counter = 0

def read_serial_data(serial_port, baud_rate, output_file):
    # Open the serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    
    data_list = [[],[],[]]

    try:
        while True:
            if ser.in_waiting > 0 and counter < 3064 :
                # Read a line from the serial port
                line = ser.readline().decode('utf-8').strip()
                
                # Split the line into components
                try:
                    data_parts = line.split(',')
                    if len(data_parts) == 3:
                        data_list[0].append( int(data_parts[0])  ) 
                        data_list[1].append( float(data_parts[1]))
                        data_list[2].append( float(data_parts[2]))
                        counter += 1

                    else:
                        print(f"Invalid data format: {line}")
                except ValueError as e:
                    print(f"Error parsing data: {e}, line: {line}")
            elif counter == 3064:
                ser.close()
                with open(output_file, 'wb') as file:
                    pickle.dump({'data':data_list},f)
                ser.open()

    except KeyboardInterrupt:
        print("Terminating...")

    finally:
        # Close the serial port
        ser.close()
        
        # Save the data to a .dat file using pickle
        with open(output_file, 'wb') as f:
            pickle.dump({'data':data_list}, f)
        print(f"Data saved to {output_file}")

# Example usage
if __name__ == "__main__":
    serial_port = '/dev/ttyUSB0'  # Replace with your serial port
    baud_rate = 115200  # Replace with your baud rate
    output_file = 'output1.dat'
    
    read_serial_data(serial_port, baud_rate, output_file)
