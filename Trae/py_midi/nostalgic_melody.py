from midiutil import MIDIFile
import random

def create_nostalgic_melody():
    # 创建MIDI文件对象，包含4个音轨
    midi = MIDIFile(4)
    
    # 设置音轨名称和乐器
    tracks = [
        {"name": "Piano", "instrument": 0},     # Acoustic Grand Piano
        {"name": "Guitar", "instrument": 25},   # Acoustic Guitar (Steel)
        {"name": "Bass", "instrument": 33},    # Electric Bass (Finger)
        {"name": "Drums", "instrument": 0}     # Standard Drum Kit (Channel 10)
    ]
    
    # 初始化音轨
    for i, track in enumerate(tracks):
        midi.addTrackName(i, 0, track["name"])
        midi.addProgramChange(i, 0, 0, track["instrument"])
    
    # 定义Am自然小调音阶和和弦进行
    scale = [57, 59, 60, 62, 64, 65, 67, 69]  # A minor scale
    chords = [
        [57, 60, 64],  # Am
        [55, 59, 62],  # Gm
        [53, 57, 60],  # Fm
        [52, 55, 59]   # Em
    ]
    
    # 生成钢琴主旋律（缓慢而忧伤）
    time = 0
    for _ in range(32):
        pitch = random.choice(scale)
        duration = random.choice([1, 1.5, 2])
        volume = random.randint(60, 80)
        midi.addNote(0, 0, pitch, time, duration, volume)
        time += duration
    
    # 生成吉他和弦（琶音进行）
    time = 0
    for _ in range(16):
        chord = random.choice(chords)
        # 为每个和弦音符添加琶音
        for i, note in enumerate(chord):
            duration = 2
            volume = random.randint(40, 60)
            midi.addNote(1, 0, note, time + i*0.5, duration-i*0.5, volume)
        time += 2
    
    # 生成贝斯音轨（稳定的低音支撑）
    time = 0
    for _ in range(16):
        chord = random.choice(chords)
        root_note = chord[0] - 12  # 降八度
        duration = 2
        volume = random.randint(50, 70)
        midi.addNote(2, 0, root_note, time, duration, volume)
        time += 2
    
    # 生成鼓组音轨（轻柔的节奏型）
    time = 0
    for _ in range(32):
        # 底鼓
        if random.random() < 0.3:
            midi.addNote(3, 9, 36, time, 0.5, random.randint(30, 50))
        # 军鼓
        if random.random() < 0.4:
            midi.addNote(3, 9, 38, time + 1, 0.5, random.randint(20, 40))
        # 闭合踩镲
        if random.random() < 0.6:
            midi.addNote(3, 9, 42, time + 0.5, 0.5, random.randint(20, 30))
        time += 2
    
    # 保存MIDI文件
    with open("nostalgic_melody.midi", "wb") as f:
        midi.writeFile(f)

if __name__ == "__main__":
    create_nostalgic_melody()
    print("MIDI文件已生成：nostalgic_melody.midi")