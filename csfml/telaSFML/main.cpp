#include <SFML/Graphics.hpp>
#include <iostream>

int main() {
    // Detectando o sistema operacional apenas para fins de log
    #if defined(_WIN32)
        std::cout << "Rodando no Windows" << std::endl;
    #elif defined(__linux__)
        std::cout << "Rodando no Linux" << std::endl;
    #endif

    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Cross-Platform!");
    sf::CircleShape shape(300.f);
    shape.setFillColor(sf::Color::Green);

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }



        window.clear();
        window.draw(shape);
        window.display();
    }

    return 0;
}
