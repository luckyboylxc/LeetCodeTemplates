#Count how many bits are set in 1 in the binary expression of x
bin(x).count("1")
#Returns the number of bits required to represent an integer in binary, excluding the sign and leading zeros.
x.bit_length()

def bitLen(x):
    length = 0
    while (x):
        x >>= 1
        length += 1
    return(length)

def bitLenCount(x):
    length = 0
    count = 0
    while (x):
        count += (x & 1)
        length += 1
        x >>= 1
    return(length, count)

# testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.
def testBit(int_type, offset):
	mask = 1 << offset
	return(int_type & mask)

# setBit() returns an integer with the bit at 'offset' set to 1.
def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)
 
 # clearBit() returns an integer with the bit at 'offset' cleared.
def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

# toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.
def toggleBit(int_type, offset):
   mask = 1 << offset
   return(int_type ^ mask)