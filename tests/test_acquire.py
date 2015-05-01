import alazar.alazar as alz
import alazar.processor as proc
import numpy as np

def do_acquire():

	b = alz.Alazar(1,1)

	b.setup_capture_clock("internal", "1 GS/s")

	b.setup_input_channels("1 V")

	b.setup_one_trigger()

    dproc = proc.BufferProcessor()

	return b.acquire(dproc,4096,65536,512,timeout=1000,buffer_count = 128)