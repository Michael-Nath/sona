import argparse
import time
import json
import numpy as np
import os
from brainflow.board_shim import BoardShim, BrainFlowInputParams

def main():
    cwd = os.getcwd()
    print(cwd)
    os.chdir(cwd)

    BoardShim.enable_dev_board_logger()

    parser = argparse.ArgumentParser()
    # use docs to check which parameters are required for specific board, e.g. for Cyton - set serial port
    
    
    parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards',
                        required=False, default=0)
    parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False, default=0)

    parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='/dev/cu.usbserial-DM03GV39')

    parser.add_argument('--mac-address', type=str, help='mac address', required=False, default='')

    parser.add_argument('--streamer-params', type=str, help='streamer params', required=False, default='')
    args = parser.parse_args()

    params = BrainFlowInputParams()
    params.timeout = args.timeout
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address
    

    board = BoardShim(args.board_id, params)
    board.prepare_session()
    # board.start_stream () # use this for default options
    board.start_stream(45000, args.streamer_params)
    time.sleep(5)
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data()  # get all data and remove it from internal buffer
    board.stop_stream()
    board.release_session()

    print(data.shape)
    np.savetxt('test_data.txt', data)
    print(data)


if __name__ == "__main__":
    main()