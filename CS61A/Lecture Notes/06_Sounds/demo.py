# 生成一个三角波声音，并把它按WAV格式写成song.wav文件，双击就能播放
from wave import open
from struct import Struct
from math import floor

# 采样率：每秒采多少个点
frame_rate = 11025


# 把浮点数振幅 → WAV需要的整数样本
def encode(x):
    i = int(16384 * x)
    # Struct("h")：把整数打包成2字节（16bit）小端整数
    return Struct("h").pack(i)


# 生成“波形函数”
# frequency：频率（Hz），决定音调高低
# amplitude：振幅，控制音量
def tri(frequency, amplitude=0.3):
    # 计算周期长度（采样点数）
    period = frame_rate // frequency

    def sampler(t):
        # 锯齿波，范围在-0.5 ~ +0.5
        saw_wav = t / period - floor(t / period + 0.5)
        # 三角波，范围在-1 ~ +1
        tri_wav = 2 * abs(2 * saw_wav) - 1
        return amplitude * tri_wav

    return sampler


# 把声音按时间采样，保存在song.wav文件中
# seconds：控制最终生成的音频文件时长（以秒为单位）
def play(sampler, name="song.wav", seconds=2):
    out = open(name, "wb")
    # 单声道
    out.setnchannels(1)
    # 每样本2字节（16bit）
    out.setsampwidth(2)
    # 采样率
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        # sampler(t)：第t个时刻的振幅
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()


c_freq, e_freq, g_freq = 261.63, 329.63, 392.00


# 将两个声音采样函数叠加
def both(f, g):
    return lambda t: f(t) + g(t)


# 两个三角波叠加后的声音
# play(both(tri(c_freq),tri(e_freq)))


# 把一个持续振荡的采样函数f，变成一个“只在[start, end]时间内发声、并且带淡入淡出”的音符采样函数
def note(f, start, end, fade=0.01):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        # 淡入
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        # 淡出
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)

    return sampler


# 根据八度生成对应音高的Mario旋律
def mario_at(octave):
    c, e = tri(octave * c_freq), tri(octave * e_freq)
    g, low_g = tri(octave * g_freq), tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)


# 按时间组合Mario旋律中的各个音符
def mario(c, e, g, low_g):
    # 音符开始的时间位置
    z = 0
    song = note(e, z, z + 1 / 8)
    z += 1 / 8
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(c, z, z + 1 / 8))
    z += 1 / 8
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(g, z, z + 1 / 4))
    z += 1 / 2
    song = both(song, note(low_g, z, z + 1 / 4))
    z += 1 / 2
    return song


if __name__ == "__main__":
    play(both(mario_at(1), mario_at(1 / 2)))
