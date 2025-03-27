from midiutil import MIDIFile
import random

def create_ocean_storm_midi():
    # 创建MIDI文件对象，包含4个音轨
    midi = MIDIFile(4)
    
    # 设置每个音轨的名称和乐器
    tracks = [
        {"name": "Ocean Waves", "instrument": 122},  # Seashore
        {"name": "Wind", "instrument": 73},         # Flute
        {"name": "Thunder", "instrument": 127},     # Gunshot
        {"name": "Strings", "instrument": 49}      # Strings
    ]
    
    # 初始化音轨
    for i, track in enumerate(tracks):
        midi.addTrackName(i, 0, track["name"])
        midi.addProgramChange(i, 0, 0, track["instrument"])
    
    # 生成海浪声音轨（低音持续音符）
    time = 0
    for _ in range(32):
        pitch = random.randint(36, 48)  # 低音区域
        duration = random.uniform(1, 2)
        volume = random.randint(60, 90)
        midi.addNote(0, 0, pitch, time, duration, volume)
        time += duration
    
    # 生成风声音轨（快速的音阶片段）
    time = 0
    for _ in range(48):
        pitch = random.randint(60, 84)
        duration = random.uniform(0.25, 0.5)
        volume = random.randint(50, 100)
        midi.addNote(1, 0, pitch, time, duration, volume)
        time += duration * 0.5
    
    # 生成雷声音轨（随机的强力打击）
    for _ in range(8):
        time = random.uniform(0, 30)
        midi.addNote(2, 0, 60, time, 0.5, 127)
    
    # 生成弦乐音轨（和弦进行）
    time = 0
    chord_base = [48, 52, 55, 60]  # Cm和弦
    for _ in range(16):
        for note in chord_base:
            duration = 2
            volume = random.randint(40, 80)
            midi.addNote(3, 0, note, time, duration, volume)
        time += 2
    
    # 保存MIDI文件
    with open("ocean_storm.midi", "wb") as f:
        midi.writeFile(f)

if __name__ == "__main__":
    create_ocean_storm_midi()
    print("MIDI文件已生成：ocean_storm.midi")