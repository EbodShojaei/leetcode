#include <stdio.h>
#include <stdlib.h>

// O(N^2) - This implementation starts from the center outwards in separate even/odd length palindromic loops 
// Note how starting from center outwards allows the while to break early, thus avoiding redundant outer checks if inner matches fail
char* longestPalindrome(char* s) {
    int start = 0, maxLen = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        // Odd-length
        int l = i, r = i;
        while (l >= 0 && s[r] != '\0' && s[l] == s[r]) {
            if (r - l + 1 > maxLen) {
                start = l;
                maxLen = r - l + 1;
            }
            l--; r++;
        }

        // Even-length
        l = i; r = i + 1;
        while (l >= 0 && s[r] != '\0' && s[l] == s[r]) {
            if (r - l + 1 > maxLen) {
                start = l;
                maxLen = r - l + 1;
            }
            l--; r++;
        }
    }

    // Allocate and copy result
    char* result = (char*)malloc(maxLen + 1);
    for (int i = 0; i < maxLen; i++) {
        result[i] = s[start + i];
    }
    result[maxLen] = '\0';
    return result;
}

// O(N^3) - original implementation moves scanner forward from start for all possible combinations (includes redundant checks e.g., s = bbba, s[1:-1] is redundant)
// Note how we don't need separate even/odd checks since we don't start from the center outwards
// char* longestPalindrome(char* s) {
//     int maxLen = 0;
//     int start = 0;

//     for (int itr1 = 0; s[itr1] != '\0'; itr1++) {
//         for (int itr2 = itr1; s[itr2] != '\0'; itr2++) {
//             int ip1 = itr1;
//             int ip2 = itr2;
//             int isPalindrome = 1;

//             while (ip1 < ip2) {
//                 if (s[ip1] != s[ip2]) {
//                     isPalindrome = 0;
//                     break;
//                 }
//                 ip1++;
//                 ip2--;
//             }

//             if (isPalindrome && (itr2 - itr1 + 1 > maxLen)) {
//                 start = itr1;
//                 maxLen = itr2 - itr1 + 1;
//             }
//         }
//     }

//     // Allocate and copy the longest palindrome substring
//     char* result = (char*)malloc(maxLen + 1);
//     for (int i = 0; i < maxLen; i++) {
//         result[i] = s[start + i];
//     }
//     result[maxLen] = '\0';

//     return result;
// }

int main() {
  printf("%s\n", longestPalindrome("babba"));
  return 0;
}
