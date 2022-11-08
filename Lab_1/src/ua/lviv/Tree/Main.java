package ua.lviv.Tree;

public class Main {
    public static void main(String[] args) {
        AVLTree tree = new AVLTree();
        tree.root = tree.insert(tree.root, 10);
        tree.root = tree.insert(tree.root, 20);
        tree.root = tree.insert(tree.root, 30);
        tree.root = tree.insert(tree.root, 40);
        tree.root = tree.insert(tree.root, 50);
        tree.root = tree.insert(tree.root, 25);
        tree.preorderPrint(tree.root);
        System.out.println("\n");
        tree.root = tree.remove(tree.root, 30);
        tree.root = tree.remove(tree.root, 40);
        tree.preorderPrint(tree.root);
    }
}
