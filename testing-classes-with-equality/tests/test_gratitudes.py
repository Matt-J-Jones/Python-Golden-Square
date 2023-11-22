from lib.gratitudes import Gratitudes

def test_creates_object():
    grattitude = Gratitudes()
    assert grattitude.format() == "Be grateful for: "

def test_creates_object_adds_item():
    grattitude = Gratitudes()
    grattitude.add("days off")
    assert grattitude.format() == "Be grateful for: days off"
  
def test_creates_object_adds_two_items():
    grattitude = Gratitudes()
    grattitude.add("days off")
    grattitude.add("lie ins")
    assert grattitude.format() == "Be grateful for: days off, lie ins"
 