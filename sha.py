import hashlib

def sha512(message):
    # Initialize hash values
    # H = [
    #     0x6a09e667f3bcc908, 0xbb67ae8584caa73b,
    #     0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
    #     0x510e527fade682d1, 0x9b05688c2b3e6c1f,
    #     0x1f83d9abfb41bd6b, 0x5be0cd19137e2179
    # ]
    IV = 0x0101010101010101  # Replace with your custom IV value
    H = [IV] * 8
    print("\n",H[0])
    print("\n",H[1])
    print("\n",H[2])
    print("\n",H[3])
    print("\n",H[4])
    print("\n",H[5])
    print("\n",H[6])
    print("\n",H[7])
    print("\n")
    # Constants
    K = [
        0x428a2f98d728ae22, 0x7137449123ef65cd,
        0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
        0x3956c25bf348b538, 0x59f111f1b605d019,
        0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
        0xd807aa98a3030242, 0x12835b0145706fbe,
        0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
        0x72be5d74f27b896f, 0x80deb1fe3b1696b1,
        0x9bdc06a725c71235, 0xc19bf174cf692694,
        0xe49b69c19ef14ad2, 0xefbe4786384f25e3,
        0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
        0x2de92c6f592b0275, 0x4a7484aa6ea6e483,
        0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
        0x983e5152ee66dfab, 0xa831c66d2db43210,
        0xb00327c898fb213f, 0xbf597fc7beef0ee4,
        0xc6e00bf33da88fc2, 0xd5a79147930aa725,
        0x06ca6351e003826f, 0x142929670a0e6e70,
        0x27b70a8546d22ffc, 0x2e1b21385c26c926,
        0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
        0x650a73548baf63de, 0x766a0abb3c77b2a8,
        0x81c2c92e47edaee6, 0x92722c851482353b,
        0xa2bfe8a14cf10364, 0xa81a664bbc423001,
        0xc24b8b70d0f89791, 0xc76c51a30654be30,
        0xd192e819d6ef5218, 0xd69906245565a910,
        0xf40e35855771202a, 0x106aa07032bbd1b8,
        0x19a4c116b8d2d0c8, 0x1e376c085141ab53,
        0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
        0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb,
        0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
        0x748f82ee5defb2fc, 0x78a5636f43172f60,
        0x84c87814a1f0ab72, 0x8cc702081a6439ec,
        0x90befffa23631e28, 0xa4506cebde82bde9,
        0xbef9a3f7b2c67915, 0xc67178f2e372532b,
        0xca273eceea26619c, 0xd186b8c721c0c207,
        0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
        0x06f067aa72176fba, 0x0a637dc5a2c898a6,
        0x113f9804bef90dae, 0x1b710b35131c471b,
        0x28db77f523047d84, 0x32caab7b40c72493,
        0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
        0x4cc5d4becb3e42b6, 0x597f299cfc657e2a,
        0x5fcb6fab3ad6faec, 0x6c44198c4a475817
    ]

    # Padding
    length = len(message) * 8  # in bits
    message += b'\x80'
    message += b'\x00' * ((112 - len(message) % 128) % 128)
    message += length.to_bytes(16, 'big')


    # Process blocks
    for i in range(0, len(message), 128):
        block = message[i:i + 128]
        
        W = [int.from_bytes(block[t:t + 8], 'big') for t in range(0, 128, 8)]
        #print(W)

         # Loop for t = 0 to 15
        for t in range(16):
            W[t] = int.from_bytes(block[t * 8:(t + 1) * 8], 'big')
            
        # Extend the message schedule
        for t in range(16, 80):
            W.append((s1(W[t-2]) + W[t-7] + s0(W[t-15]) + W[t-16]) % (2**64))

        # Initialize the working variables
        a, b, c, d, e, f, g, h = H

        # Main loop
        for t in range(15):
            T1 = (h + Ch(e, f, g) + s1(e) + W[t] + K[t]) % (2**64)
            T2 = (s0(a) + Maj(a, b, c)) % (2**64)
            h = g
            g = f
            f = e
            e = (d + T1) % (2**64)
            d = c
            c = b
            b = a
            a = (T1 + T2) % (2**64)
           


        # Update hash values
        H[0] = (H[0] + a) % (2**64)
        H[1] = (H[1] + b) % (2**64)
        H[2] = (H[2] + c) % (2**64)
        H[3] = (H[3] + d) % (2**64)
        H[4] = (H[4] + e) % (2**64)
        H[5] = (H[5] + f) % (2**64)
        H[6] = (H[6] + g) % (2**64)
        H[7] = (H[7] + h) % (2**64)
        print("\n H[0]=",H[0])
        print("\n H[1]=",H[1])
        print("\n H[2]=",H[2])
        print("\n H[3]=",H[3])
        print("\n H[4]=",H[4])
        print("\n H[5]=",H[5])
        print("\n H[6]=",H[6])
        print("\n H[7]=",H[7])
        print("\n")

    # Convert the hash values to bytes
    hash_bytes = b''.join(h.to_bytes(8, 'big') for h in H)
    print("\n",hash_bytes)
    return hash_bytes

# Utility functions
def Ch(x, y, z):
    return (x & y) ^ (~x & z)

def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def s0(x):
    return (x >> 1 | (x << 63)) ^ (x >> 8 | (x << 56)) ^ (x >> 7)

def s1(x):
    return (x >> 19 | (x << 45)) ^ (x >> 61 | (x << 3)) ^ (x >> 6)

# Example usage
#message = b"20L-1377-Maida Shahid-35202-7166376-8"



# Provided hexadecimal string
# hex_string = (
#     "3636363636363636"
#     "3636363636363636"
#     "3636363636363636"
#     "3636363636363636"
#     "3636363636363636"
#     "3636363636363636"
#     "3636363636363636"
#     "3636363636363363"
#     "6363636363636363"
#     "6363636363636363"
#     "6363636363636363"
#     "6363636363636336"
#     "3636363636363636"
#     "3636363636363636"
#     "3636363636363636"
#     "3637333f34363636"
#     "02004C2D01030707"
#     "2D4D5A6564612020"
#     "53696169642D0305"
#     "0200022D07010606"
#     "0307062D08800000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000000"
#     "0000000000000128"
# )



hex_string = (
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5c5c5c5c5c5c"
    "5c5c5d59555e5c5c"
    "9e0ac827abc52ff2"
    "6d3974cdeea28899"
    "9f6bc443cb7a26b5"
    "6355fd4ecfa1f84e"
    "55c05cb3c111ead2"
    "5aec7b5df1727efe"
    "Fe1c6025add19203"
    "f5a894b935fef30a"
    "0000000000000000"
    "0000000000000000"
    "0000000000000000"
    "0000000000000000"
    "0000000000000000"
    "0000000000000000"
    "0000000000000000"
    "0000000000000000"
)

# Convert hex string to bytes
message = bytes.fromhex(hex_string)
print("Message:", message.hex())
hashed = sha512(message)
print("SHA-512:", hashed.hex())


# import hashlib
# import hmac

# def hmac_sha512(key, message):
#     block_size = 128  # For SHA-512, block size is 128 bytes
#     sha512_size = 64  # SHA-512 produces a 64-byte (512-bit) hash

#     # Step 1: Key Padding
    
#     if len(key) > block_size:
#         key = hashlib.sha512(key).digest()
#     elif len(key) < block_size:
#         key = key.ljust(block_size, b'\x00')
#     # Step 2: Inner Padding
#     inner_padding = bytes(x ^ 0x36 for x in key)
#     # Step 3: Outer Padding
#     outer_padding = bytes(x ^ 0x5C for x in key)

#     # Step 4: Inner Hash
#     inner_hash_input = inner_padding + message
#     inner_hash = hashlib.sha512(inner_hash_input).digest()

#     # Step 5: Outer Hash
#     outer_hash_input = outer_padding + inner_hash
#     final_hash = hashlib.sha512(outer_hash_input).hexdigest()

#     return final_hash

# # Example usage
# secret_key = b'15092000'
# message_to_authenticate = b'Hello, world!'
# result_hmac = hmac_sha512(secret_key, message_to_authenticate)
# print("\n",result_hmac)


