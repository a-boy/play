#include <stdio.h>
#include <threads.h>

int func(void* arg) {
    printf("Printing from Thread\n");
    return NULL;
}

int main() {
    thrd_t thread_id;
    thrd_create(&thread_id, func, NULL);
    thrd_join(thread_id, NULL);  // Wait for thread to return before continuing execution
    printf("Thread returned\n");
    return 0;
}