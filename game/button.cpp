#include <raylib.h>
#include <stdio.h>

int fight(int atk, int def, int type1, int type2);
void home();
void arena();
void eventMouseHome();
void eventMouseArena();
int hover(int x1, int x2, int y1, int y2);
void changecolor(int button);
void selectItems(int typeItems);

int level[10];
int step = 1;
struct color{
    int r=255, g=0, b=0;
}rgb[30];
int money=100;
int type = 0;
int hp_player = 200, hp_boss = 200;
int boss[4][2] = {{30, 20}, {30, 20}, {30, 20}, {30, 20}};
int player[] = {40, 20, 40, 20};
int items[] = {0, 0, 0, 0};
int price[] = {20, 20, 20, 20};

int main(){
    const int WindowWidth = 1280;
    const int WindowHeight = 720;
    for (int i=0; i < 10; i++)
        level[i] = 1;
    
    InitWindow(WindowWidth, WindowHeight, "My Game");
    SetTargetFPS(60);
    while (!WindowShouldClose()){
        if (step == 1){
            home();
            eventMouseHome();
        }
        if (step == 2){
            arena();
            eventMouseArena();
        }
    }
    return 0;
}

int fight(int atk, int def, int type1, int type2){
    int result;
    if (type1 == type2)
        result = atk - def;
    else
        result = atk + (def/2) - def;
    return result;
}

void home(){
    BeginDrawing();
    ClearBackground(RAYWHITE);
    DrawRectangle(500, 100, 100, 100, Color{rgb[0].r, rgb[0].g, rgb[0].b, 255}); //player
    DrawRectangle(500, 250, 100, 100, Color{rgb[1].r, rgb[1].g, rgb[1].b, 255});
    DrawRectangle(500, 400, 100, 100, Color{rgb[2].r, rgb[2].g, rgb[2].b, 255});
    DrawRectangle(500, 550, 100, 100, Color{rgb[3].r, rgb[3].g, rgb[3].b, 255});
    DrawRectangle(1000, 550, 80, 80, Color{rgb[4].r, rgb[4].g, rgb[4].b, 255});
    DrawText(FormatText("Lv. %d", level[0]), 520, 180, 20, BLACK);
    DrawText(FormatText("Lv. %d", level[1]), 520, 330, 20, BLACK);
    DrawText(FormatText("Lv. %d", level[2]), 520, 480, 20, BLACK);
    DrawText(FormatText("Lv. %d", level[3]), 520, 630, 20, BLACK);
    DrawRectangle(1000, 200, 80, 80, Color{rgb[5].r, rgb[5].g, rgb[5].b, 255});
    DrawRectangle(1100, 200, 80, 80, Color{rgb[6].r, rgb[6].g, rgb[6].b, 255});
    DrawRectangle(1000, 300, 80, 80, Color{rgb[7].r, rgb[7].g, rgb[7].b, 255});
    DrawRectangle(1100, 300, 80, 80, Color{rgb[8].r, rgb[8].g, rgb[8].b, 255});
    DrawText(FormatText("$ %d", price[0]), 400, 150, 30, GREEN);
    DrawText(FormatText("$ %d", price[1]), 400, 300, 30, GREEN);
    DrawText(FormatText("$ %d", price[2]), 400, 450, 30, GREEN);
    DrawText(FormatText("$ %d", price[3]), 400, 600, 30, GREEN);
    DrawText(FormatText("money: %d", money), 10, 20, 50, GREEN);
    EndDrawing();
}

void arena(){
    BeginDrawing();
    ClearBackground(RAYWHITE);
    DrawRectangle(100, 200, 200, 200, BLUE); //player
    DrawRectangle(800, 200, 200, 200, GREEN); //boss
    EndDrawing();
}

void eventMouseHome(){
    if (hover(500, 600, 100, 200) && money >= price[0]){
        changecolor(0);
        type = 1;
    }
    else if (hover(500, 600, 250, 350) && money >= price[1]){
        changecolor(1);
        type = 2;
    }
    else if (hover(500, 600, 400, 500) && money >= price[2]){
        changecolor(2);
        type = 3;
    }
    else if (hover(500, 600, 550, 650) && money >= price[3]){
        changecolor(3);
        type = 4;
    }
    else if (hover(1000, 1080, 550, 630)){
        changecolor(4);
        type = 5;
    }
    else if (hover(1000, 1080, 200, 280))
        type = 6;
    else if (hover(1100, 1180, 200, 280))
        type = 7;
    else if (hover(1000, 1080, 300, 380))
        type = 8;
    else if (hover(1100, 1180, 300, 380))
        type = 9;
    else{
        type = 0;
        for (int i=0; i < 5; i++){
            rgb[i].r = 255;
            rgb[i].g = 0;
            rgb[i].b = 0;
        }
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 1){
        level[0]++;
        price[0] += 20;
        money -= 20;
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 2){
        level[1]++;
        price[1] += 20;
        money -= 20;
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 3){
        level[2]++;
        price[2] += 20;
        money -= 20;
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 4){
        level[3]++;
        price[3] += 20;
        money -= 20;
    }
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 5)
        step = 2;
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 6)
        selectItems(1);
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 7)
        selectItems(2);
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 8)
        selectItems(3);
    if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && type == 9)
        selectItems(4);
}

void eventMouseArena(){
    
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