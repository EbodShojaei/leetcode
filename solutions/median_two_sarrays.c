#include <stdio.h>

double findMedianSortedArrays(int *nums1, int nums1Size, int *nums2, int nums2Size) {
  int idx_1 = 0;
  int idx_2 = 0;
  int val1 = 0;
  int val2 = 0;
  int total_s = nums1Size + nums2Size;
  double result = -1.0;
  double temp = 0.0;

  for (int i = 0; i <= total_s / 2; i++) {
    temp = result;

    // Check bounds first, then assign valid comparison values
    if (idx_1 >= nums1Size) {
      val1 = nums2[idx_2];
      result = val1;
      idx_2++;
    } else if (idx_2 >= nums2Size) {
      val1 = nums1[idx_1];
      result = val1;
      idx_1++;
    } else if (nums1[idx_1] < nums2[idx_2]) {
      val1 = nums1[idx_1];
      result = val1;
      idx_1++;
    } else {
      val2 = nums2[idx_2];
      result = val2;
      idx_2++;
    }

    if (total_s % 2 == 0 && i == total_s / 2) {
      result = (result + temp) / 2.0;
      return result;
    }
  }

  return result;
}

int main(void) { 
  int nums1[] = {1, 2};
  int nums2[] = {3, 4};
  printf("%f\n", findMedianSortedArrays(nums1, 2, nums2, 2));  // Output: 2.5

  return 0;
}
