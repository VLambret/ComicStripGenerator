from Model.PanelItem import PanelItem

POSITIONS = [
    {'expected': (0, 0), 'pixel': '0, 0', 'percentage': '0%, 0%', 'natural': 'left'},
    {'expected': (200, 0), 'pixel': '200, 0', 'percentage': '50%, 0%', 'natural': 'middle'},
    {'expected': (400, 0), 'pixel': '400, 0', 'percentage': '100%, 0%', 'natural': 'right'},
    {'expected': (0, 100), 'pixel': '0, 100', 'percentage': '0%, 50%', 'natural': 'center-left'},
    {'expected': (200, 100), 'pixel': '200, 100', 'percentage': '50%, 50%', 'natural': 'center'},
    {'expected': (400, 100), 'pixel': '400, 100', 'percentage': '100%, 50%', 'natural': 'center-right'},
    {'expected': (0, 200), 'pixel': '0, 200', 'percentage': '0%, 100%', 'natural': 'top-left'},
    {'expected': (200, 200), 'pixel': '200, 200', 'percentage': '50%, 100%', 'natural': 'top'},
    {'expected': (400, 200), 'pixel': '400, 200', 'percentage': '100%, 100%', 'natural': 'top-right'},
    ]

def get_boxed_position_100x200_image(pos, box):
    return PanelItem("test/red_100x200.png", pos).get_position_in_box(box)

def test_boxed_pixel_position():
    for pos in POSITIONS:
        pixel_pos = get_boxed_position_100x200_image(pos['pixel'], (500, 400))
        percent_pos = get_boxed_position_100x200_image(pos['percentage'], (500, 400))
        natural_pos = get_boxed_position_100x200_image(pos['natural'], (500, 400))

        assert pixel_pos == pos['expected'], "pixel position is not affected by box size"
        assert percent_pos == pos['expected'], "test percentage position"
        assert natural_pos == pos['expected'], "test natural position"
