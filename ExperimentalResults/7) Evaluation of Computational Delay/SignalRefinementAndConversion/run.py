from Preprocessing import Preprocessing 
from SignalRefinement import SignalRefinement 
from SampleConversion import SampleConversion
import time

''' 
To better align with the processing steps in the paper, we divided the data processing into two completely independent steps (running two scripts separately). This resulted in redundant data saving and reading, so the theoretical time calculated by this script will be greater than the actual time (as in practice, the two steps are integrated).
''' 

def main():
    directory = "Dataset_NeckPass"
    Preprocessing(directory)
    start_time = time.time()

    SignalRefinement(directory)    # This step will read the dataset and save it.
    SampleConversion(directory + "_filtered")     # This step will read the dataset and save it.

    end_time = time.time()
    duration = end_time - start_time
    return duration

if __name__ == "__main__":

    duration = main()

    print(f"Generation - Total time(120s): {duration:.6f} seconds")
    print(f"Generation - One-second sample time(1s): {(duration/120):.6f} seconds")
