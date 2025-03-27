from midiutil import MIDIFile
import random

def create_piano_melody():
    # 创建MIDI文件对象，包含2个音轨（主旋律和伴奏）
    midi = MIDIFile(2)
    
    # 设置音轨名称和乐器（使用钢琴音色）
    tracks = [
        {"name": "Melody", "instrument": 0},    # Acoustic Grand Piano
        {"name": "Accompaniment", "instrument": 0}
    ]
    
    # 初始化音轨
    for i, track in enumerate(tracks):
        midi.addTrackName(i, 0, track["name"])
        midi.addProgramChange(i, 0, 0, track["instrument"])
    
    # 定义音阶和和弦进行
    scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C大调音阶
    chords = [
        [60, 64, 67],  # C大三和弦
        [67, 71, 74],  # G大三和弦
        [65, 69, 72],  # F大三和弦
        [62, 65, 69]   # Dm和弦
    ]
    
    # 生成主旋律
    time = 0
    for _ in range(32):
        # 从音阶中选择音符
        pitch = random.choice(scale)
        # 变化音符时值，创造节奏感
        duration = random.choice([0.5, 1, 1.5])
        # 控制音量变化，使旋律更有表现力
        volume = random.randint(80, 100)
        midi.addNote(0, 0, pitch, time, duration, volume)
        time += duration
    
    # 生成和弦伴奏
    time = 0
    for _ in range(16):
        # 选择和弦
        chord = random.choice(chords)
        # 为每个和弦音符添加音符
        for note in chord:
            duration = 2
            volume = random.randint(50, 70)
            midi.addNote(1, 0, note, time, duration, volume)
        time += 2
    
    # 保存MIDI文件
    with open("piano_melody.midi", "wb") as f:
        midi.writeFile(f)

if __name__ == "__main__":
    create_piano_melody()
    print("MIDI文件已生成：piano_melody.midi")