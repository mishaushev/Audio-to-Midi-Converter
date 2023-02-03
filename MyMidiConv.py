from pydub import AudioSegment
import pretty_midi

# Load audio file
audio_file = AudioSegment.from_file("Save Your Soul 2023 Acapella.mp3", format="mp3")

# Extract audio data and sample rate from the file
audio_data = audio_file.raw_data
sample_rate = audio_file.frame_rate

# Create a PrettyMIDI object from the audio data
midi_object = pretty_midi.fluidsynth(audio_data, sample_rate)

# Save the MIDI data to a file
midi_object.write("example.mid")
