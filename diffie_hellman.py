class DiffieHellman:
    shared_prime = 23
    shared_base = 5

    alice_secret = 6
    bob_secret = 15

    print("public variables: ")
    print('shared prime: ', shared_prime, '\nshared base: ', shared_base)
    
    alice = (shared_base**alice_secret) % shared_prime

    print('Alice sends: ', alice)

    bob = (shared_base**bob_secret) % shared_prime

    print('Bob sends: ', bob)

    alice_shared_secret = (bob ** alice_secret) % shared_prime
    print('Alice shared secret: ', alice_shared_secret)

    bob_shared_secret = (alice ** bob_secret) % shared_prime
    print('Bob shared secret: ', bob_shared_secret)

if __name__ == "__main__":
    dh = DiffieHellman()
