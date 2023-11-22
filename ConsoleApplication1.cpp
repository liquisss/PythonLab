#include <iostream>
#include <unordered_map>


void sieveOfEratosthenes(int n) {
    std::unordered_map<int, bool> prime; 
    // Создаем ассоциативный контейнер для хранения чисел и их статуса (простое или составное)

    for (int i = 2; i <= n; i++) {
        prime[i] = true; // Инициализируем все числа от 2 до n как простые
    }

    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) { // Если число p является простым
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false; // Вычеркиваем все кратные числа p как составные
            }
        }
    }

    std::cout << "Простые числа от 2 до " << n << ":\n";
    for (int i = 2; i <= n; i++) {
        if (prime[i]) {
            std::cout << i << " "; // Выводим все простые числа от 2 до n
        }
    }
    
}

int main() {
    setlocale(LC_ALL, "Russian");
    int n;
    std::cout << "Введите верхнюю границу диапазона: ";
    std::cin >> n;

    sieveOfEratosthenes(n);

    return 0;
}