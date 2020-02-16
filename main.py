import pygame
from pygame.locals import *
import sys
from pprint import *
import time
import Data_Bar
import readcsvfile


def main():
    pygame.init()
    bg_size = (800, 800)
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    MAX_BAR_NUM = 10
    file = readcsvfile.data_list('danmu_an.csv')
    datas = file.analyze()[-50:]
    font = pygame.font.Font('msyh.ttf', 15)
    screen = pygame.display.set_mode(bg_size)
    turn = 1
    # s.fill(BLACK)
    clock = pygame.time.Clock()
    key = -1
    delay = 1000
    bars = []
    temp_delete = []
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        # 更新数据
        delay -= 1
        if not(delay % 50):
            key += turn
            if key >= len(datas):
                # turn = -1
                key = len(datas) - 1
            if key <= 0:
                # turn = 1
                pass
            date = datas[key][0]
            name_list = [x[0] for x in datas[key][1:]]
            value_list = [x[1] for x in datas[key][1:]]
            sort_list = sorted(zip(name_list, value_list), key=lambda x: x[1], reverse=True)
            name_list = [x[0] for x in sort_list]
            value_list = [x[1] for x in sort_list]
            rank_list = range(MAX_BAR_NUM)
            data_dic = {}
            # 生成数据字典
            for name, value, rank in zip(name_list, value_list, rank_list):
                data_dic[name] = {
                    'value': value,
                    'rank': rank
                }
            # pprint(data_dic)
            # 图中已有数据条
            # bars = []
            delete = []
            temp = []
            for bar in bars:
                if bar.name in data_dic:
                    bars[bars.index(bar)].update(data_dic[bar.name]['rank'], data_dic[bar.name]['value'], value_list[0])
                    # data_dic.pop(bar.name)
                    delete.append(bar.name)
                else:
                    temp.append(bar)
            # 剩余的为图中未出现数据条 -> 新增数据条
            for name in data_dic:
                if name in delete:
                    continue
                bar = Data_Bar.Bar(name)
                bar.sudden(data_dic[name]['rank']+3, data_dic[name]['value'] * 0.25, value_list[0])
                bar.update(data_dic[name]['rank'], data_dic[name]['value'], value_list[0])
                bars.append(bar)
            # 删除多余条
            for bar in temp:
                bars[bars.index(bar)].update(MAX_BAR_NUM+1, 0, value_list[0])
        screen.fill(WHITE)
        for bar in bars:
            bar.draw()
            if bar.show['y'] <= (MAX_BAR_NUM) * bar.margin:
                screen.blit(bar.data_bar, (100, bar.show['y']))
                name_font = font.render(bar.name, True, (0, 0, 0))
                value_font = font.render(str(int(bar.show['value'])), True, (0, 0, 0))
                screen.blit(name_font, (90-len(bar.name.strip()) * 15, bar.show['y']))
                screen.blit(value_font, (bar.show['width']+110, bar.show['y']-2))
            else:
                temp_delete.append(bars[bars.index(bar)])
        # 此处有未知BUG
        for bar in temp_delete:
            try:
                bars.remove(bar)
            except:
                pass
        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    start = time.time()
    main()
    print('%.2fs' % (time.time() - start))