#include<stdio.h>
#include<time.h>
int binarysearch(int arr[],int n,int key){
    int low = 0,high = n-1,mid;
    while (low<=high){
        mid=(low + high) / 2;
        if(arr[mid] == key)
        return mid;
    else if(arr[mid] < key)
    keylow =mid+1;
else
high = mid-1;
    }
    return -1;//not found
}
int main(){
    int n,key,i;
    printf("Enter number of elements:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter sorted elements:\n");
    for (i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter element to search:");
    scanf("%d",&key);
    clock_t start,end;
    start=clock();//start time
    int result = binarysearch(arr,n,key);
    end = clock();
    double time_taken = ((double)(end - start)) / CLOCK_PER_SEC;
    if(result == -1)
    printf("Element not found\n");
else
printf("Element found at index %d\n",result);
printf("Time taken:%f second\n",time_taken);
return 0;
}