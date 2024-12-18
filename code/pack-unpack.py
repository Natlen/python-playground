# * for iteratable
# ** for dictionaries (key : val)
# unpacking always creates a list, even if from a tuple

def pack_args(*args, **kwargs) -> None:
    print(args)
    print(kwargs)

pack_args(1,2,3,4,5,6,a=1,b=2,c=3)

def unpack_args_iteratable(x : int, y: float, z : list) -> None:
    print(x, y, z)
   
args1 = (1,2,[1,2,3,4])
unpack_args_iteratable(*args1)

def unpack_args_dict(key_val1 : dict[str, int], key_val2 : dict[str, int]) -> None: 
    print(key_val1, key_val2)

args2 = {"key_val1": 111111, "key_val2": "222222"}
unpack_args_dict(**args2)

l1 = [1,2,3,4,5,6,7,8,9,10]
t1 = (1,2,3,4,5,6,7,8,9,10)

def pack_partial(l : list | tuple) -> None:
    first, *mid, last = l
    print(first)
    print(mid)
    print(last)

pack_partial(l1)
pack_partial(t1)