#include <raylib.h>
#include <stdio.h>
#include <string.h>

float fight(int atk, int def, int type1, int type2);
void delayFight();
void delayBuff(int type_buff, char text[]);
void delayAnimetion(int frame);
void home();
void arena();
void resultGame();
void eventMouseHome();
void eventArena();
int hover(int x1, int x2, int y1, int y2);
void changecolor(int button);
void selectItems(int typeItems);
void randomBoss();
void item_change();

int level[10];
int step = 1;
struct color{
    int r=255, g=0, b=0;
}rgb[30];
int money = 0;
int type = 0;
int lv[] = {1, 0, 0, 0, 0};
float hp_player_bar = 200, hp_boss_bar = 200;
int hp_player = 200, hp_boss = 180;
int boss[4][2] = {{35, 20}, {35, 20}, {35, 20}, {35, 20}};
int type_boss[] = {0, 0};
int player[] = {40, 20, 40, 20};
int items[] = {0, 0, 0, 0};
int price[] = {20, 20, 20, 20};
int type_player[] = {0, 0};
char omen[20];
int buff[] = {0, 0, 0, 0};
int items_fight[2][2];
int step_arena=0;
int count = 1;
int text_boss;
int price_lv = 10;
char buff_textB[5];
int buff_posit = 100;
Texture2D sword, armor, wand, shield, eye, man;

int main(){
    const int WindowWidth = 1280;
    const int WindowHeight = 720;
    for (int i=0; i < 10; i++)
        level[i] = 1;
    
    InitWindow(WindowWidth, WindowHeight, "My Game");
    SetTargetFPS(60);
    randomBoss();
    selectItems(1);
    selectItems(3);
    strcpy(omen, "");
    strcpy(buff_textB, "");
    sword = LoadTexture("img/sword.png");
    armor = LoadTexture("img/armor.png");
    wand = LoadTexture("img/wand.png");
    shield = LoadTexture("img/shield.png");
    eye = LoadTexture("img/eye.png");
    man = LoadTexture("img/frame_player/frame1.png");
    while (!WindowShouldClose()){
        item_change();
        if (step == 1){
            home();
            eventMouseHome();
            if (step_arena == 0)
                delayAnimetion(6);
        }
        if (step == 2){
            arena();
            eventArena();
            if (step_arena == 1){
                delayFight();
            }
            if (step_arena == 2){
                delayBuff(2, "+ATK");
            }
            if (step_arena == 3){
                delayBuff(3, "+DEF");
            }
        }
        if (step == 3)
            resultGame();
    }
    return 0;
}

float fight(int atk, int def, int type1, int type2){
    float result;
    if (type1 == type2)
        result = atk - def;
    else
        result = atk + (def/2) - def;
    if (result <= 10){
        result = 10;
    }
    return result;
}

void delayFight(){
    static float time = 0.0f;
    time += GetFrameTime();
    if (time >= 0.5f){
        if (count%2 == 0){
            hp_player_bar -= (fight(items_fight[1][0]+buff[2], items_fight[0][1]+buff[1], type_player[1], type_boss[0])/hp_player)*200;
        }
        if (hp_player_bar > 200)
            hp_boss_bar = 200;
        time = 0.0f;
        count++;
    }
    if (count >= 3){
        strcpy(buff_textB, "");
        step_arena = 0;
    }
}

void delayBuff(int type_buff, char text[]){
    static float time = 0.0f;
    time += GetFrameTime();
    if (time >= 0.5f){
        if (count == 2)
            buff[type_buff] += GetRandomValue(2, 5);
        if (type_buff == 2){
            strcpy(buff_textB, text);
            rgb[10].r = 255, rgb[10].g = 0, rgb[10].b = 0;
            buff_posit = 900;
        }
        if (type_buff == 3){
            strcpy(buff_textB, text);
            rgb[10].r = 0, rgb[10].g = 0, rgb[10].b = 255;
            buff_posit = 900;
        }
        time = 0.0f;
        count++;
    }
    if (count >= 3){
        strcpy(buff_textB, "");
        step_arena = 0;
    }
}

void delayAnimetion(int frame){
    static char count = '1';
    static float time = 0.0f;
    char select[29];
    strcpy(select, "img/frame_player/frame");
    time += GetFrameTime();
    if (time >= 0.1f){
        count++;
        time = 0.0f;
    }
    if (count - 48 > frame)
        count = '1';
    select[22] = count;
    strcat(select, ".png");
    printf("%s\n", select);
    man = LoadTexture(select);
}

void home(){
    BeginDrawing();
    ClearBackground(RAYWHITE);
    DrawRectangle(500, 100, 100, 100, Color{rgb[0].r, rgb[0].g, rgb[0].b, 255}); //player
    DrawRectangle(500, 250, 100, 100, Color{rgb[1].r, rgb[1].g, rgb[1].b, 255});
    DrawRectangle(500, 400, 100, 100, Color{rgb[2].r, rgb[2].g, rgb[2].b, 255});
    DrawRectangle(500, 550, 100, 100, Color{rgb[3].r, rgb[3].g, rgb[3].b, 255});
    DrawRectangle(800, 550, 80, 80, Color{rgb[4].r, rgb[4].g, rgb[4].b, 255});
    DrawText(FormatText("Lv. %d", level[0]), 520, 200, 20, BLACK);
    DrawText(FormatText("Lv. %d", level[1]), 520, 350, 20, BLACK);
    DrawText(FormatText("Lv. %d", level[2]), 520, 500, 20, BLACK);
    DrawText(FormatText("Lv. %d", level[3]), 520, 650, 20, BLACK);
    DrawRectangle(900, 250, 100, 100, Color{rgb[5].r, rgb[5].g, rgb[5].b, 255});
    DrawRectangle(1050, 250, 100, 100, Color{rgb[6].r, rgb[6].g, rgb[6].b, 255});
    DrawRectangle(900, 400, 100, 100, Color{rgb[7].r, rgb[7].g, rgb[7].b, 255});
    DrawRectangle(1050, 400, 100, 100, Color{rgb[8].r, rgb[8].g, rgb[8].b, 255});
    DrawRectangle(700, 0, 30, 730, Color{0, 0, 0, 255});
    DrawText(FormatText("$ %d", price[0]), 400, 150, 30, GREEN);
    DrawText(FormatText("$ %d", price[1]), 400, 300, 30, GREEN);
    DrawText(FormatText("$ %d", price[2]), 400, 450, 30, GREEN);
    DrawText(FormatText("$ %d", price[3]), 400, 600, 30, GREEN);
    DrawText(FormatText("money: %d $", money), 10, 20, 50, GREEN);
    DrawText(FormatText("$ 10"), 750, 85, 40, GREEN);
    //DrawText(FormatText("%d %d", type_boss[0], type_boss[1]), 50, 300, 50, RED);
    DrawRectangle(850, 80, 80, 80, Color{rgb[9].r, rgb[9].g, rgb[9].b, 255});
    DrawText(FormatText("%s", omen), 940, 110, 30, RED);
    DrawTextureEx(man, Vector2{40, 100},0, 0.5, RAYWHITE);
    DrawTexture(sword, 500, 100, RAYWHITE);
    DrawTexture(armor, 500, 250, RAYWHITE);
    DrawTexture(wand, 500, 400, RAYWHITE);
    DrawTexture(shield, 500, 550, RAYWHITE);
    DrawTexture(eye, 850, 80, RAYWHITE);
    DrawTexture(sword, 900, 250, RAYWHITE);
    DrawTexture(wand, 1050, 250, RAYWHITE);
    DrawTexture(armor, 900, 400, RAYWHITE);
    DrawTexture(shield, 1050, 400, RAYWHITE);
    EndDrawing();
}

void arena(){
    BeginDrawing();
    ClearBackground(RAYWHITE);
    DrawRectangle(100, 200, 200, 200, BLUE); //player
    DrawRectangle(900, 200, 200, 200, GREEN); //boss
    DrawText(FormatText("%d %d", type_player[0], type_player[1]), 500, 100, 50, RED);
    DrawText(FormatText("%d %d", type_boss[0], type_boss[1]), 500, 200, 50, RED);
    DrawText(FormatText("%s", buff_textB), buff_posit, 150, 40, Color{rgb[10].r, rgb[10].g, rgb[10].b, 255});
    DrawRectangle(100, 450, hp_player_bar, 30, RED); //hp player
    DrawRectangle(900, 450, hp_boss_bar, 30, RED); //hp boss
    DrawText(FormatText("Lv. %d", text_boss), 900, 100, 40, BLACK);
    DrawText(FormatText("Lv. %d", lv[0]), 100, 100, 40, BLACK);
    DrawRectangleLinesEx(Rectangle{100, 450, 200, 30}, 5, BLACK); //border hp player
    DrawRectangleLinesEx(Rectangle{900, 450, 200, 30}, 5, BLACK); //border hp boss
    DrawRectangleLinesEx(Rectangle{400, 550, 100, 100}, 3, BLACK);
    DrawRectangleLinesEx(Rectangle{550, 550, 100, 100}, 3, BLACK);
    DrawRectangleLinesEx(Rectangle{700, 550, 100, 100}, 3, BLACK);
    EndDrawing();
}

void resultGame(){
    int price_lv=0;
    int sur=0;
    int total=0;
    int go=0;
    for (int i=0; i < 3; i++)
        buff[i] = 0;
    price_lv += text_boss*10;
    if (type_player[0] == type_boss[1])
        sur += text_boss*10;
    if (type_player[1] != type_boss[0])
        sur += text_boss*10;
    total += 100+price_lv+sur;
    BeginDrawing();
    ClearBackground(RAYWHITE);
    DrawText(FormatText("Winner +%d $", 100+price_lv), 400, 100, 50, GREEN);
    DrawText(FormatText("Bonus survivor +%d $", sur), 400, 200, 50, GREEN);
    DrawText(FormatText("Total %d $", total), 400, 300, 50, GREEN);
    if (hover(400, 700, 550, 660)){
        DrawRectangle(400, 550, 300, 100, WHITE);
        DrawText("Go Home", 420, 570, 60, BLACK);
        go = 1;
    }
    else{
        DrawRectangle(400, 550, 300, 100, BLACK);
        DrawText("Go Home", 420, 570, 60, WHITE);
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && go == 1){
        hp_player += 20;
        randomBoss();
        money += total;
        lv[0]++;
        hp_boss_bar = 200;
        hp_player_bar = 200;
        strcpy(omen, "");
        count = 1;
        step_arena = 0;
        if (type_boss[0] == 0 && type_boss[1] == 0)
            boss[0][0] += 5+GetRandomValue(1, 4), boss[0][1] += 5+GetRandomValue(1, 4);
        if (type_boss[0] == 0 && type_boss[1] == 1)
            boss[1][0] += 5+GetRandomValue(1, 4), boss[1][1] += 5+GetRandomValue(1, 4);
        if (type_boss[0] == 1 && type_boss[1] == 0)
            boss[2][0] += 5+GetRandomValue(1, 4), boss[2][1] += 5+GetRandomValue(1, 4);
        if (type_boss[0] == 1 && type_boss[1] == 1)
            boss[3][0] += 5+GetRandomValue(1, 4), boss[3][1] += 5+GetRandomValue(1, 4);
        step = 1;
    }
    EndDrawing();
}

void eventMouseHome(){
    if (hover(500, 600, 100, 200) && money - price[0] >= 0){
        changecolor(0);
        type = 1;
    }
    else if (hover(500, 600, 250, 350) && money - price[1] >= 0){
        changecolor(1);
        type = 2;
    }
    else if (hover(500, 600, 400, 500) && money - price[2] >= 0){
        changecolor(2);
        type = 3;
    }
    else if (hover(500, 600, 550, 650) && money - price[3] >= 0){
        changecolor(3);
        type = 4;
    }
    else if (hover(800, 880, 550, 630)){
        changecolor(4);
        type = 5;
    }
    else if (hover(900, 1000, 250, 350))
        type = 6;
    else if (hover(1050, 1150, 250, 350))
        type = 7;
    else if (hover(900, 1000, 400, 500))
        type = 8;
    else if (hover(1050, 1150, 400, 500))
        type = 9;
    else if (hover(850, 930, 80, 160)){
        changecolor(9);
        type = 10;
    }
    else{
        type = 0;
        for (int i=0; i < 15; i++){
            if (i < 5 || i > 8){
                rgb[i].r = 255;
                rgb[i].g = 0;
                rgb[i].b = 0;
            }
        }
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 1){
        level[0]++;
        player[0] += 5 + GetRandomValue(1, 3);
        money -= price[0];
        price[0] += 20;
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 2){
        level[1]++;
        player[1] += 5 + GetRandomValue(1, 3);
        money -= price[1];
        price[1] += 20;
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 3){
        level[2]++;
        player[2] += 5 + GetRandomValue(1, 3);
        money -= price[2];
        price[2] += 20;
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 4){
        level[3]++;
        player[3] += 5 + GetRandomValue(1, 3);
        money -= price[3];
        price[3] += 20;
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 5){
        step = 2;
        if (type_player[0] == 0)
            items_fight[0][0] = player[0];
        if (type_player[0] == 1)
            items_fight[0][0] = player[2];
        if (type_player[1] == 0)
            items_fight[0][1] = player[1];
        if (type_player[1] == 1)
            items_fight[0][1] = player[3];
        if (type_boss[0] == 0 && type_boss[1] == 0){
            items_fight[1][0] = boss[0][0], items_fight[1][1] = boss[0][1];
            lv[1]++;
            text_boss = lv[1];
            hp_boss = 200+lv[1]*20;
        }
        if (type_boss[0] == 0 && type_boss[1] == 1){
            items_fight[1][0] = boss[1][0], items_fight[1][1] = boss[1][1];
            lv[2]++;
            text_boss = lv[2];
            hp_boss = 200+lv[2]*20;
        }
        if (type_boss[0] == 1 && type_boss[1] == 0){
            items_fight[1][0] = boss[2][0]+5, items_fight[1][1] = boss[2][1];
            lv[3]++;
            text_boss = lv[3];
            hp_boss = 200+lv[3]*20;
        }
        if (type_boss[0] == 1 && type_boss[1] == 1){
            items_fight[1][0] = boss[3][0], items_fight[1][1] = boss[3][1];
            lv[4]++;
            text_boss = lv[4];
            hp_boss = 200+lv[4]*20;
        }
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 6)
        selectItems(1);
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 7)
        selectItems(2);
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 8)
        selectItems(3);
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 9)
        selectItems(4);
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 10){
        int item = GetRandomValue(0, 1);
        if (type_boss[item] == 0)
            strcpy(omen, "physical");
        if (type_boss[item] == 1)
            strcpy(omen, "magic");
    }
}

void eventArena(){
    if (hp_boss_bar <= 0){
        step = 3;
        price_lv += text_boss*10;
    }
    if (IsKeyPressed(KEY_A) && step_arena == 0){
        hp_boss_bar -= (fight(items_fight[0][0]+buff[0], items_fight[1][1]+buff[3], type_player[0], type_boss[1])/hp_boss)*200;
        count = 1;
        step_arena = 1;
    }
    if (IsKeyPressed(KEY_S) && step_arena == 0){
        int action = GetRandomValue(1, 4);
        buff[0] += GetRandomValue(5, 10);
        strcpy(buff_textB, "+ATK");
        rgb[10].r = 255, rgb[10].g = 0, rgb[10].b = 0;
        buff_posit = 100;
        if (action == 3){
            count = 1;
            step_arena = 1;
        }
        if (action == 4){
            count = 1;
            step_arena = 2;
        }
        if (action <= 2){
            count = 1;
            step_arena = 3;
        }
    }
    if (IsKeyPressed(KEY_D) && step_arena == 0){
        int action = GetRandomValue(1, 4);
        buff[1] += GetRandomValue(5, 10);
        strcpy(buff_textB, "+DEF");
        rgb[10].r = 0, rgb[10].g = 0, rgb[10].b = 255;
        buff_posit = 100;
        if (action == 3){
            count = 1;
            step_arena = 1;
        }
        if (action <= 2){
            count = 1;
            step_arena = 2;
        }
        if (action == 4){
            count = 1;
            step_arena = 3;
        }
    }
}

int hover(int x1, int x2, int y1, int y2){
    int mx = GetMouseX();
    int my = GetMouseY();
    if (mx > x1 && mx < x2 && my > y1 && my < y2)
        return 1;
    else
        return 0;
}

void changecolor(int button){
    rgb[button].r = 250;
    rgb[button].g = 125;
    rgb[button].b = 85;
}

void selectItems(int typeItems){
    man = LoadTexture("img/frame_player/frame1.png");
    if (typeItems == 1)
        items[typeItems-1] = 1;
    if (typeItems == 2)
        items[typeItems-1] = 1;
    if (typeItems == 3)
        items[typeItems-1] = 1;
    if (typeItems == 4)
        items[typeItems-1] = 1;

    if (typeItems == 1 && items[1] == 1)
        items[1] = 0;
    if (typeItems == 2 && items[0] == 1)
        items[0] = 0;
    if (typeItems == 3 && items[3] == 1)
        items[3] = 0;
    if (typeItems == 4 && items[2] == 1)
        items[2] = 0;
    for (int i=0; i < 4; i++){
        if (items[i] == 1){
            rgb[i+5].r = 250;
            rgb[i+5].g = 125;
            rgb[i+5].b = 85;
        }
        else{
            rgb[i+5].r = 250;
            rgb[i+5].g = 0;
            rgb[i+5].b = 0;
        }
    }
}

void randomBoss(){
    type_boss[0] = GetRandomValue(0, 1);
    type_boss[1] = GetRandomValue(0, 1);
}

void item_change(){
    if (items[0] == 1)
        type_player[0] = 0;
    if (items[1] == 1)
        type_player[0] = 1;
    if (items[2] == 1)
        type_player[1] = 0;
    if (items[3] == 1)
        type_player[1] = 1;
}