def terrain_update(left_tile, right_tile) :
    left_tile.update()
    right_tile.update()
        
    if left_tile.get_rightx() < 0:
        left_tile.set_leftx(right_tile.get_rightx())
    elif right_tile.get_rightx() < 0:
        right_tile.set_leftx(left_tile.get_rightx())