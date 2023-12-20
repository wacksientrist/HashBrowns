#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void utf8ToBinary(FILE *outputFile, const char *utf8String) {
    while (*utf8String != '\0') {
        unsigned char utf8Char = (unsigned char)(*utf8String);

        for (int i = 7; i >= 0; i--) {
            fprintf(outputFile, "%d", (utf8Char & (1 << i)) ? 1 : 0);
        }

        fprintf(outputFile, "");

        utf8String++;
    }

    fprintf(outputFile, "");
}

int main() {
    const char *filename = "INP";
    const char *outputFilename = "Buffer";

    FILE *file = fopen(filename, "r");
    FILE *outputFile = fopen(outputFilename, "w");

    if (!file) {
        perror("Error opening input file");
        return 1;
    }

    if (!outputFile) {
        perror("Error opening output file");
        fclose(file);
        return 1;
    }

    fseek(file, 0, SEEK_END);
    long fileSize = ftell(file);
    rewind(file);

    char *utf8String = (char *)malloc(fileSize + 1);

    if (!utf8String) {
        perror("Memory allocation error");
        fclose(file);
        fclose(outputFile);
        return 1;
    }

    fread(utf8String, 1, fileSize, file);
    utf8String[fileSize] = '\0';

    fclose(file);

    //fprintf(outputFile, "UTF-8 String from file %s:\n%s\n", filename, utf8String);
    fprintf(outputFile, "");
    utf8ToBinary(outputFile, utf8String);

    free(utf8String);
    fclose(outputFile);

    return 0;
}
