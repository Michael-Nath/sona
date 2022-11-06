import argparse
import time
import json
import numpy as np
import pandas as pd
import os
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from datetime import date

from pprint import pprint
import matplotlib.pyplot as plt


DURATION = 30 # seconds to record data for

def config_board():

    board_idD = BoardIds.CYTON_BOARD.value
    pprint(BoardShim.get_board_descr(board_idD))
    cwd = os.getcwd()
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

    board_id = BoardIds.CYTON_BOARD.value

    params = BrainFlowInputParams()
    params.timeout = args.timeout
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address
    board = BoardShim(args.board_id, params)
    board.prepare_session()

    return board, args


def stream(board, args, duration):
    
    # board.start_stream () # use this for default options
    board.start_stream(45000, args.streamer_params)
    time.sleep(duration)
    
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data()  # get all data and remove it from internal buffer
    
    board.stop_stream()
    board.release_session()

    emg_channels = BoardShim.get_emg_channels(BoardIds.CYTON_BOARD.value)
    df = pd.DataFrame(np.transpose(data))
    
    plt.figure()
    df[emg_channels].plot(subplots=True)
    plt.savefig('before_processing.png')
    print('Data From the Board')
    print(df.head(10))
    
    

    return data

def save_data(data):
    date_abbrev = date.today().strftime("%b-%d-%Y")
    np.savetxt('tested' + date_abbrev + '.csv', data)

    return 'tested' + date_abbrev + '.csv'

    
    
def main():
    print(time.time)

    board, args = config_board()
    print(time.time)

    data = stream(board, args, DURATION)
    print(time.time)
    filename = save_data(data)
    print(board.get_emg_channels(board.board_id))
    print(time.time)

if __name__ == "__main__":
    main()
    print("Completed!")