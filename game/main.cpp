#include <raylib.h>
#include <stdio.h>

int fight(int atk, int def, int type1, int type2);

int main(){
    const int WindowWidth = 1280;
    const int WindowHeight = 720;
    
    InitWindow(WindowWidth, WindowHeight, "My Game");
    SetTargetFPS(60);
    int hp_player = 200, hp_boss = 200;
    int player[] = {40, 10};
    int boss[] = {40, 10};
    int count = 2;
    while (!WindowShouldClose()){
        BeginDrawing();
        ClearBackground(RAYWHITE);
        static float time = 0.0f;
        DrawRectangle(100, 200, 200, 200, BLUE); //player
        DrawRectangle(800, 200, 200, 200, GREEN); //boss
        DrawRectangle(100, 450, hp_player, 30, RED); //hp player
        DrawRectangle(800, 450, hp_boss, 30, RED); //hp boss
        DrawRectangleLinesEx(Rectangle{100, 450, 200, 30}, 5, BLACK); //border hp player
        DrawRectangleLinesEx(Rectangle{800, 450, 200, 30}, 5, BLACK); //border hp boss
        time += GetFrameTime();
        if (time >= 1.0f && hp_player > 0 && hp_boss > 0){
            if (count%2 == 0)
                hp_boss -= fight(player[0], boss[1], 1, 0);
            else
                hp_player -= fight(boss[0], player[1], 0, 0);
            printf("%d %d\n", hp_player, hp_boss);
            time = 0.0f;
            count++;
        }
        //DrawRectangle(1000, 200, 200, 200, RED);
        EndDrawing();
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