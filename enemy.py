from pico2d import *
import random
import game_framework
import game_world
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import server

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Enemy:
    image = None

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image('./png/turtle_1.png')
        self.x, self.y = random.randint(300, 500), random.randint(0, 1) * 800
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0
        self.build_behavior_tree()

    def wander(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 1.0
            self.dir = random.random() * 2 * math.pi  # 방향을 라디안 값으로 설정
            return BehaviorTree.SUCCESS
        return BehaviorTree.SUCCESS
        # else:
        #     return BehaviorTree.RUNNING
        pass

    def find_player(self):
        # fill here
        distance2 = (server.character.x - self.x) ** 2 + (server.character.y - self.y) ** 2
        if distance2 <= (PIXEL_PER_METER * 10) ** 2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def move_to_player(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.dir = math.atan2(server.character.y - self.y, server.character.x - self.x)
        return BehaviorTree.SUCCESS  # 일단 소년쪽으로 이동만 해도 성공으로 여긴다

    def build_behavior_tree(self):
        # fill here
        wander_node = LeafNode('Wander', self.wander)

        find_player_node = LeafNode('Find Player', self.find_player)
        move_to_player_node = LeafNode('Move to Player', self.move_to_player)
        chase_node = SequenceNode('Chase')
        chase_node.add_children(find_player_node, move_to_player_node)

        chase_wander_node = SelectorNode('Chase or Wander')
        chase_wander_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(wander_node)

        pass

    def update(self):
        # fill here
        self.bt.run()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(0 + 10, self.x, 800 - 10)
        self.y = clamp(0 + 15, self.y, 600 - 15)
        if 520 < self.y < 600:
            self.x = clamp(365 + 10, self.x, 440 - 10)
        if 0 < self.x < 365 - 2:
            self.y = clamp(0 + 45, self.y, 520 - 15)
        if 0 < self.y < 40:
            self.x = clamp(365 + 10, self.x, 440 - 10)
        if 440 < self.x < 800:
            self.y = clamp(0 + 45, self.y, 520 - 15)

    def draw(self):
        if 0 <= math.cos(self.dir) < 1:
            if 0 <= math.sin(self.dir) < (2**1/2)/4:
                self.image.clip_draw(int(self.frame) * 32, 32 * 5, 32, 32, self.x, self.y)
            if (2**1/2)/4 <= math.sin(self.dir) < 3*(2**1/2)/4:
                self.image.clip_draw(int(self.frame) * 32, 32 * 6, 32, 32, self.x, self.y)
            if 3*(2**1/2)/4 <= math.sin(self.dir) < 1:
                self.image.clip_draw(int(self.frame) * 32, 32 * 7, 32, 32, self.x, self.y)

            if -(2**1/2)/4 <= math.sin(self.dir) < 0:
                self.image.clip_draw(int(self.frame) * 32, 32 * 5, 32, 32, self.x, self.y)
            if -3 * (2**1/2)/4 <= math.sin(self.dir) < -(2**1/2)/4:
                self.image.clip_draw(int(self.frame) * 32, 32 * 4, 32, 32, self.x, self.y)
            if -1 <= math.sin(self.dir) < -3 * (2**1/2)/4:
                self.image.clip_draw(int(self.frame) * 32, 32 * 3, 32, 32, self.x, self.y)

        if -1 <= math.cos(self.dir) < 0:
            if 0 <= math.sin(self.dir) < (2**1/2)/4:
                self.image.clip_draw(int(self.frame) * 32, 32 * 1, 32, 32, self.x, self.y)
            if (2**1/2)/4 <= math.sin(self.dir) < 3*(2**1/2)/4:
                self.image.clip_draw(int(self.frame) * 32, 32 * 0, 32, 32, self.x, self.y)
            if 3*(2**1/2)/4 <= math.sin(self.dir) < 1:
                self.image.clip_draw(int(self.frame) * 32, 32 * 7, 32, 32, self.x, self.y)

            if -(2**1/2)/4 <= math.sin(self.dir) < 0:
                self.image.clip_draw(int(self.frame) * 32, 32 * 2, 32, 32, self.x, self.y)
            if -3 * (2**1/2)/4 <= math.sin(self.dir) < -(2**1/2)/4:
                self.image.clip_draw(int(self.frame) * 32, 32 * 1, 32, 32, self.x, self.y)
            if -1 <= math.sin(self.dir) < -3 * (2**1/2)/4:
                self.image.clip_draw(int(self.frame) * 32, 32 * 3, 32, 32, self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 10, self.y + 15

    def handle_collision(self, other, group):
        if group == 'star:enemies':
            game_world.remove_object(self)
