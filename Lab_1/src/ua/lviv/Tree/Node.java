package ua.lviv.Tree;

class Node {
    int key;
    int height;
    Node right = null;
    Node left = null;

    Node (int key) {
        this.key = key;
        this.height = 1;
    }
}
