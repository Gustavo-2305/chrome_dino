def terrain_update(left_tile, right_tile) :
    left_tile.update()
    right_tile.update()
        
    if left_tile.get_right() < 0:
        left_tile.set_left(right_tile.get_right())
    elif right_tile.get_right() < 0:
        right_tile.set_left(left_tile.get_right())