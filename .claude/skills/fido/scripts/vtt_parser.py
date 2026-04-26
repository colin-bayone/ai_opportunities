"""
VTT Parser for Teams Transcripts.
Ported from communications/transcript_services/vtt_parser.py.

Parses Microsoft Teams VTT transcript format into structured utterances.
Zero external dependencies — stdlib only.

Usage:
    parser = VTTParser(vtt_content)
    parser.parse()

    print(f"Found {len(parser.utterances)} utterances")
    print(f"Speakers: {', '.join(parser.get_speakers())}")
    stats = parser.get_speaker_stats()
"""
import re
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Utterance:
    """Single spoken segment with speaker, text, and timing."""
    speaker: str
    text: str
    start_time: float  # seconds
    end_time: float    # seconds
    sequence: int
    word_count: int

    def duration(self) -> float:
        return self.end_time - self.start_time


class VTTParser:
    """
    Parse Teams VTT transcripts into structured utterances.

    Handles the Microsoft Teams VTT format:
    - WEBVTT header and metadata
    - Timestamp format: HH:MM:SS.mmm --> HH:MM:SS.mmm
    - Speaker tags: <v Speaker Name>Text content</v>
    """

    def __init__(self, vtt_content: str):
        self.vtt_content = vtt_content
        self.utterances: List[Utterance] = []
        self._parsed = False

    def parse_timestamp(self, timestamp: str) -> float:
        """Convert VTT timestamp to seconds."""
        try:
            parts = timestamp.strip().split(':')
            if len(parts) == 3:
                hours = int(parts[0])
                minutes = int(parts[1])
                seconds = float(parts[2])
                return hours * 3600 + minutes * 60 + seconds
        except (ValueError, IndexError):
            pass
        return 0.0

    def parse(self) -> List[Utterance]:
        """Parse VTT content and extract structured utterances."""
        if self._parsed:
            return self.utterances

        self.utterances = []
        lines = self.vtt_content.split('\n')

        i = 0
        sequence = 0

        # Skip WEBVTT header and metadata lines
        while i < len(lines) and '-->' not in lines[i]:
            i += 1

        while i < len(lines):
            line = lines[i].strip()

            if '-->' in line:
                try:
                    start_str, end_str = line.split('-->')
                    start_time = self.parse_timestamp(start_str)
                    end_time = self.parse_timestamp(end_str)

                    i += 1
                    if i < len(lines):
                        text_line = lines[i].strip()

                        speaker_match = re.match(r'<v\s+([^>]+)>(.*?)</v>', text_line)
                        if speaker_match:
                            speaker = speaker_match.group(1).strip()
                            text = speaker_match.group(2).strip()

                            if text:
                                utterance = Utterance(
                                    speaker=speaker,
                                    text=text,
                                    start_time=start_time,
                                    end_time=end_time,
                                    sequence=sequence,
                                    word_count=len(text.split()),
                                )
                                self.utterances.append(utterance)
                                sequence += 1
                except (ValueError, IndexError):
                    pass

            i += 1

        self._parsed = True
        return self.utterances

    def get_speakers(self) -> List[str]:
        """Get unique speakers in order of appearance."""
        if not self._parsed:
            self.parse()

        seen = set()
        speakers = []
        for utt in self.utterances:
            if utt.speaker not in seen:
                speakers.append(utt.speaker)
                seen.add(utt.speaker)
        return speakers

    def get_speaker_stats(self) -> Dict[str, Dict]:
        """Calculate speaking statistics per speaker."""
        if not self._parsed:
            self.parse()

        stats = {}
        total_words = sum(utt.word_count for utt in self.utterances)

        for utt in self.utterances:
            if utt.speaker not in stats:
                stats[utt.speaker] = {
                    'utterance_count': 0,
                    'word_count': 0,
                    'total_duration': 0.0,
                    'percentage': 0.0,
                }
            stats[utt.speaker]['utterance_count'] += 1
            stats[utt.speaker]['word_count'] += utt.word_count
            stats[utt.speaker]['total_duration'] += utt.duration()

        for speaker in stats:
            if total_words > 0:
                stats[speaker]['percentage'] = (
                    stats[speaker]['word_count'] / total_words
                ) * 100

        return stats

    def get_duration(self) -> float:
        """Get total transcript duration in seconds."""
        if not self._parsed:
            self.parse()
        if not self.utterances:
            return 0.0
        return self.utterances[-1].end_time

    def get_utterances_by_speaker(self, speaker: str) -> List[Utterance]:
        """Get all utterances from a specific speaker."""
        if not self._parsed:
            self.parse()
        return [utt for utt in self.utterances if utt.speaker == speaker]

    def __len__(self) -> int:
        if not self._parsed:
            self.parse()
        return len(self.utterances)

    def __repr__(self) -> str:
        if self._parsed:
            return f"<VTTParser: {len(self.utterances)} utterances, {len(self.get_speakers())} speakers>"
        return "<VTTParser: not parsed>"
