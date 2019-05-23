import wave

# infiles = ["test1.wav", "test2.wav"]

def tidalwave(infiles, outfile):
	with wave.open(outfile, 'wb') as wav_out: #+확장자
		for wav_path in infiles: #파일 경로 + 확장자 
			with wave.open(wav_path, 'rb') as wav_in:
			if not wav_out.getnframes():
				wav_out.setparams(wav_in.getparams())
				wav_out.writeframes(wav_in.readframes(wav_in.getnframes()))