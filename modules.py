import algo_pack
from algo_pack import swap
from algo_pack import *         # by default does not import _ methods
from algo_pack import _internal # (JavaScript-style) private functions are loaded when requested

print __name__
print algo_pack.__name__
print algo_pack.swap.__name__

print swap(5, 10)
_internal()
print "Haha. I can."
