# Challenge Description:
1. Hey Smitty inmates used me in Second IndoChina war.
2. My owner used me to hide messages that were revealing authorship in the First Folio.

# Methodology to Solve
    - Each of the sentences in the description are assumed to be hints related to ciphers that are required to solve the challenge
        - The first sentence mentions the name 'Smitty' and the Second IndoChina war. 
            - The Second IndoChina war is another name for the Vietnam war and 'Smitty' references Captain Carlyle "Smitty" Harris. The Captain used a cipher called 'Tap Code' to communicate with other POWs when he was trapped in a POW camp. 
            - Tap Code uses a 5x5 Polybius square with the number of knocks being used as a coordinate system
            
              |__1__|__2__|__3__|__4__|__5__|
            1 |  A  |  B  |  C  |  D  |  E  |
            2 |  F  |  G  |  H  |  I  | J/K |
            3 |  L  |  M  |  N  |  O  |  P  |
            4 |  Q  |  R  |  S  |  T  |  U  |
            5 |  V  |  W  |  X  |  Y  |  Z  |

        - The second sentence references the 'First Folio' and hidden messages.
            - A google search for 'First Folio Cryptology' lead to an article describing the Francis Bacon Society.
            - Members of this society believe Francis Bacon was the true author of Shakespeare's works. Francis Bacon was also known for the Baconian Cipher
            - This is essentially binary using the letters A and B.
                - E.g. A = aaaaa , B = aaaab
    
    - Now that we know the ciphers being used, we translate the dots using tap code (given that the word knock is a delimeter) and then place the resulting ciphertext into a baconian cipher decoder
    - This produces the answer