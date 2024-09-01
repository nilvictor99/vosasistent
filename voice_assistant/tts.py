import soundfile as sf
from nemo.collections.tts.models import FastPitchModel
from nemo.collections.tts.models import HifiGanModel

fastpitch_name = "tts_es_fastpitch_multispeaker"
hifigan_name = "tts_es_hifigan_ft_fastpitch_multispeaker"

spec_generator = FastPitchModel.from_pretrained(fastpitch_name)
vocoder = HifiGanModel.from_pretrained(hifigan_name)

def generate_speech(text: str, speaker: int, acoustic_model=spec_generator, vocoder=vocoder):
    """
    Generate speech audio waveform from text input.

    Parameters
    ----------
    text : str
        The input text to be converted into speech.
    speaker : int
        The speaker ID to use for speech synthesis.
    acoustic_model : object, optional
        The model used to generate the spectrogram from text (default is `spec_generator`).
    vocoder : object, optional
        The model used to convert the spectrogram to audio waveform (default is `model`).

    Returns
    -------
    np.ndarray
        The generated audio waveform as a NumPy array.
    """
    parsed = spec_generator.parse(text, normalize=False)
    spectrogram = spec_generator.generate_spectrogram(tokens=parsed, speaker=speaker)
    audio_waveform = model.convert_spectrogram_to_audio(spec=spectrogram)
    audio_waveform = audio_waveform.detach().cpu().numpy()
    return audio_waveform
