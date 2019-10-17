import math
def reward_function(params):
    track_width = params['track_width']                   #트랙의 폭 (미터 단위)
    distance_from_center = params['distance_from_center'] #트랙 중심으로부터 절대 거리. 
    steering = abs(params['steering_angle'])              #자동차의 조향각도
    direction_stearing=params['steering_angle']           #자동차 방향
    speed = params['speed']                               #속도
    steps = params['steps']                               #스텝
    progress = params['progress']                         #주행완료 백분율
    all_wheels_on_track = params['all_wheels_on_track']   #네바퀴 모두 트랙위에 있는지
    is_left_of_center = params['is_left_of_center']       #트랙 센터의 좌측에 있는지 여부
    # Read input variables
    waypoints = params['waypoints']                       #트랙 중앙을 따라 있는 waypoint들의 (x,y) 좌표 목록(ordered list). 리스트의 인덱스는 0부터 시작합니다.
    closest_waypoints = params['closest_waypoints']       #가까운 이전 waypoint인덱스와 가까운 다음 waypoint의 인덱스를 목록으로 반환합니다. params['closest_waypoints'][0] 는 가까운 이전 waypoint의 인덱스를 반환하고, params['closest_waypoints'][1] 는 가까운 다음 waypoint의 인덱스를 반환합니다.
    heading = params['heading']                           #자동차가 진행하고 있는 방향을 알려줍니다 (단위: degree). 자동차가 x-축이 증가하는 방향(즉, y축 값은 상수)을 보고 있다면, 리턴값은 0가 됩니다. y-축이 증가하는 방향(x-축은 상수)을 바라보면 90이, y-축의 값이 줄어드는 방향(x-축은 상수)을 바라고 있는 경우, -90이 반환됩니다.
    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]          #다음 웨이포인트
    prev_point = waypoints[closest_waypoints[0]]          #이전 웨이포인트
    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    # Penalize the reward if the difference is too large
    
    DIRECTION_THRESHOLD = 10.0
    # ABS_STEERING_THRESHOLD = 15
    # SPEED_TRESHOLD = 5
    # TOTAL_NUM_STEPS = 85
    reward = 1.0
    if progress == 100:
      reward += 100
    malus=1
    if direction_diff > DIRECTION_THRESHOLD:
      malus=1-(direction_diff/50)
    if malus<0 or malus>1:
      malus = 0
    reward *= malus
    return reward
