#include<stdio.h>
#include<stdlib.h>
#include<time.h>
//Liner search
int linersearch(int arrr[],int n, int key){
    for (int i=0;i<n;i++){
        if(arr[i] == key)
        return i;
    }
    return -1;
}
int main(){
    int n,key,result;
    clock_t start ,end;
    double time_taken;
    print("Enter number of element :");
    scanf("%d",&n)
    int *arr = (int*)malloc(n * sizeof(int));
    //random value
    for(int i=0;i<n;i++){
        arr[i] = rand() % 10000;
    }
    printf("Enter element to search:");
    scanf("&d",&key);
    //clculat the time
    start = clock();
    result = linersearch(arr,n,key);
    end =clock();
    time_taken = ((double)(end -start)) / CLOCK_PER_SEC;
    if(result == -1)
    printf("Element not found\n");
else
printf("Element found at index %d\n",result);
printf("Time taken: %f seconds \n",time_taken);
free(arr);
return 0;
}