#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>

/**
  * infinite_while - infinite print
  * Return: 0 when terminated
  */
int infinite_while(void)
{
	while (1)
    {
        sleep(1);
    }
	return (0);
}

/**
  * main - create 5 zombie processes
  * Return: 0 when terminated
  */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}
