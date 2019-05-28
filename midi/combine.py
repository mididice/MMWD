import wave
import contextlib
import os


def tidalwave(base_dir, infiles, outfile):
    with wave.open(outfile, 'wb') as wav_out: #+확장자
        for wav_path in infiles: #파일 경로 + 확장자
            wave_file = os.path.join(base_dir, wav_path + ".wav")
            with wave.open(wave_file, 'rb') as wav_in:
                if not wav_out.getnframes():
                    wav_out.setparams(wav_in.getparams())
                wav_out.writeframes(wav_in.readframes(wav_in.getnframes()))


def durationwave(outfile):
    with contextlib.closing(wave.open(outfile, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration