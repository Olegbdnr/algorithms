package ua.lviv.Tree;

class AVLTree {
    Node root = null;

    int getHeight(Node node) {
        if (node != null) {
            return node.height;
        }
        return 0;
    }

    int getBalanceFactor(Node node) {
        return getHeight(node.right) - getHeight(node.left);
    }

    void fixHeight(Node node) {
        int leftHeight = getHeight(node.left);
        int rightHeight = getHeight(node.right);
        node.height = (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
    }

    Node rotateRight(Node parent) {
        Node leftChild = parent.left;
        parent.left = leftChild.right;
        leftChild.right = parent;
        fixHeight(parent);
        fixHeight(leftChild);
        return leftChild;
    }

    /*        x              y
    *        / \            / \
    *       y   T3  --->   T1  x
    *      / \      <---      /  \
    *     T1  T2             T2   T3
    * */

    Node rotateLeft(Node parent) {
        Node rightChild = parent.right;
        parent.right = rightChild.left;
        rightChild.left = parent;
        fixHeight(parent);
        fixHeight(rightChild);
        return rightChild;
    }

    Node balance(Node node) {
        fixHeight(node);
        if (getBalanceFactor(node) == 2) {
            if (getBalanceFactor(node.right) < 0) {
                node.right = rotateRight(node.right);
            }
            return rotateLeft(node);
        }
        if (getBalanceFactor(node) == -2) {
            if (getBalanceFactor(node.left) > 0) {
                node.left = rotateLeft(node.left);
            }
            return rotateRight(node);
        }
        return node;
    }

    Node insert(Node node, int key) {
        if (node == null) {
            return new Node(key);
        }
        if (key > node.key) {
            node.right = insert(node.right, key);
        }
        if (key < node.key) {
            node.left = insert(node.left, key);
        }
        return balance(node);
    }

    Node findMin(Node node) {
        if (node.left == null) {
            return node;
        }
        return findMin(node.left);
    }

    Node removeMin(Node node) {
        if (node.left == null) {
            return node.right;
        }
        node.left = removeMin(node.left);
        return balance(node);
    }

    Node remove(Node node, int key) {
        if (node == null) {
            return node;
        }
        if (key < node.key) {
            node.left = remove(node.left, key);
        }
        if (key > node.key) {
            node.right = remove(node.right, key);
        }
        if (key == node.key) {
            Node leftChild = node.left;
            Node rightChild = node.right;
            node = null;
            if (rightChild == null) {
                return leftChild;
            }
            Node min = findMin(rightChild);
            min.right = removeMin(rightChild);
            min.left = leftChild;
            return balance(min);
        }
        return balance(node);
    }

    void preorderPrint(Node node) {
        if (node != null) {
            System.out.println(node.key);
            preorderPrint(node.right);
            preorderPrint(node.left);
        }
    }
}