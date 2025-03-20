#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define PLAYER_NUM 3
#define CARD_NUM 16
#define HAND_CARDS 16

typedef struct {
    char suit;
    int value;
} Card;

typedef struct {
    Card hand[HAND_CARDS];
    int cardCount;
} Player;

Card deck[52];
Player players[PLAYER_NUM];
int currentPlayer = 0;
Card lastPlay[HAND_CARDS];
int lastPlayCount = 0;

void initializeDeck() {
    char suits[] = {'♠', '♥', '♦', '♣'};
    int index = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 3; j <= 15; j++) {
            deck[index].suit = suits[i];
            deck[index].value = j;
            index++;
        }
    }
}

void shuffleDeck() {
    srand(time(NULL));
    for (int i = 51; i > 0; i--) {
        int j = rand() % (i + 1);
        Card temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }
}

void dealCards() {
    for (int i = 0; i < PLAYER_NUM; i++) {
        players[i].cardCount = HAND_CARDS;
        for (int j = 0; j < HAND_CARDS; j++) {
            players[i].hand[j] = deck[i * HAND_CARDS + j];
        }
    }
}

void printCard(Card card) {
    char* faces[] = {"3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"};
    printf("%c%s ", card.suit, faces[card.value - 3]);
}

void printPlayerHand(int playerIndex) {
    printf("玩家 %d 的手牌: ", playerIndex + 1);
    for (int i = 0; i < players[playerIndex].cardCount; i++) {
        printCard(players[playerIndex].hand[i]);
    }
    printf("\n");
}

int compareCards(const void* a, const void* b) {
    return ((Card*)b)->value - ((Card*)a)->value;
}

void sortPlayerHand(int playerIndex) {
    qsort(players[playerIndex].hand, players[playerIndex].cardCount, sizeof(Card), compareCards);
}

int isValidPlay(Card* play, int count) {
    if (count == 0) return 0;
    if (lastPlayCount == 0) return 1;
    if (count != lastPlayCount) return 0;
    return play[0].value > lastPlay[0].value;
}

void removeCardsFromHand(int playerIndex, Card* play, int count) {
    for (int i = 0; i < count; i++) {
        for (int j = 0; j < players[playerIndex].cardCount; j++) {
            if (players[playerIndex].hand[j].suit == play[i].suit && 
                players[playerIndex].hand[j].value == play[i].value) {
                for (int k = j; k < players[playerIndex].cardCount - 1; k++) {
                    players[playerIndex].hand[k] = players[playerIndex].hand[k + 1];
                }
                players[playerIndex].cardCount--;
                break;
            }
        }
    }
}

int playTurn(int playerIndex) {
    printf("\n玩家 %d 的回合\n", playerIndex + 1);
    printPlayerHand(playerIndex);

    Card play[HAND_CARDS];
    int count = 0;
    char input[50];
    printf("请选择要出的牌（输入牌的索引，从1开始，用空格分隔，或输入'pass'）：");
    fgets(input, sizeof(input), stdin);

    if (strncmp(input, "pass", 4) == 0) {
        if (lastPlayCount == 0) {
            printf("第一个玩家不能过牌！\n");
            return 0;
        }
        printf("玩家 %d 选择过牌\n", playerIndex + 1);
        return 1;
    }

    char* token = strtok(input, " \n");
    while (token != NULL) {
        int index = atoi(token) - 1;
        if (index >= 0 && index < players[playerIndex].cardCount) {
            play[count++] = players[playerIndex].hand[index];
        }
        token = strtok(NULL, " \n");
    }

    if (!isValidPlay(play, count)) {
        printf("无效的出牌！请重试。\n");
        return 0;
    }

    printf("玩家 %d 出牌: ", playerIndex + 1);
    for (int i = 0; i < count; i++) {
        printCard(play[i]);
    }
    printf("\n");

    removeCardsFromHand(playerIndex, play, count);
    memcpy(lastPlay, play, sizeof(Card) * count);
    lastPlayCount = count;

    return 1;
}

void playGame() {
    initializeDeck();
    shuffleDeck();
    dealCards();

    printf("跑得快游戏开始！\n\n");

    for (int i = 0; i < PLAYER_NUM; i++) {
        sortPlayerHand(i);
        printPlayerHand(i);
    }

    while (1) {
        if (playTurn(currentPlayer)) {
            if (players[currentPlayer].cardCount == 0) {
                printf("\n玩家 %d 获胜！\n", currentPlayer + 1);
                break;
            }
            currentPlayer = (currentPlayer + 1) % PLAYER_NUM;
            if (lastPlayCount > 0) {
                lastPlayCount = 0;
            }
        }
    }
}

int main() {
    playGame();
    return 0;
}

