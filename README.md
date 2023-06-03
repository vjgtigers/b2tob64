This package allows for custom encoding between base2 (bianary) and base 64. <br>
WARNING: THIS WILL NOT TRANSLATE other b64 encodings and will NOT be able to encode/decode the same values <br>
<br>
<br>
Ex. "10101010101000010111111001" --> "ppE9AA" --> "10101010101000010111111001"
<br><br>
Approx. 6x len reduction


<br>

Docs<br>
function b2tob64 requires a single string input of only 1's and 0's <br>
This will return a b64 string (NOTE: this can most likely be decoded ONLY by this program)<br>
<br>
<br>
<br>
function b64tob2 requires a single b64 string input created by the b2tob64 function. <br>
this will return the original binary string.
