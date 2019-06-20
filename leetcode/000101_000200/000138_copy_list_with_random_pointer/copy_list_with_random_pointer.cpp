#include <iostream>
#include <map>

using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};

class Solution {
public:
    // Node* copyRandomList(Node* head) {
    //     if (head == NULL) return NULL;

    //     map<Node*, Node*> ptr_map;

    //     // 建立旧地址node和新地址node的对应table
    //     Node* ptr = head;
    //     while (ptr) {
    //         ptr_map[ptr] = new Node(ptr->val, NULL, NULL);
    //         ptr = ptr->next;
    //     }

    //     // 根据旧地址, 建立新地址node之间关系
    //     for (auto i = ptr_map.begin(); i != ptr_map.end(); i++) {
    //         Node* old_ptr = i->first;
    //         Node* new_ptr = i->second;

    //         Node* old_next = old_ptr->next;
    //         Node* old_random = old_ptr->random;
    //         if (old_next != NULL) {
    //             new_ptr->next = ptr_map[old_next];
    //         }
    //         if (old_random != NULL) {
    //             new_ptr->random = ptr_map[old_random];
    //         }
    //     }

    //     return ptr_map[head];
    // }
    Node* copyRandomList(Node* head) {
        if (head == NULL) return NULL;

        // 用来记录已经拷贝的节点
        map<Node*, Node*> copied_nodes;

        // 初始化
        Node* old_pre_node = head;
        Node* old_cur_node = head->next;
        copied_nodes[head] = new Node(head->val, NULL, NULL);

        while (old_cur_node) {

            Node* new_cur_node;
            auto cur_iter = copied_nodes.find(old_cur_node);
            if (cur_iter != copied_nodes.end()) {
                // 当前旧节点已经拷贝过, 直接从map中取值
                Node* new_pre_node = copied_nodes[old_pre_node];
                new_cur_node = cur_iter->second;
                new_pre_node->next = new_cur_node;
            } else {
                // 没拷贝过, 拷贝一个新node, 将pre_node指向cur_node
                new_cur_node = new Node(old_cur_node->val, NULL, NULL);
                copied_nodes[old_cur_node] = new_cur_node;
                copied_nodes[old_pre_node]->next = new_cur_node;
            }

            if (old_cur_node->random != NULL) {
                // 如果当前节点有random指针, 处理一次, 思考: 为何必须要处理, 为何处理一次即可
                auto ran_iter = copied_nodes.find(old_cur_node->random);
                if (ran_iter != copied_nodes.end()) {
                    // 如果当前节点的random指针指向的之前拷贝过节点, 则复制地址即可
                    new_cur_node->random = ran_iter->second;
                } else {
                    // 如果指向的是未拷贝的节点, 则拷贝一次
                    Node* ran_node = new Node(old_cur_node->random->val, NULL, NULL);
                    copied_nodes[old_cur_node->random] = ran_node;
                    copied_nodes[old_cur_node]->random = ran_node;
                }
            }

            old_pre_node = old_cur_node;
            old_cur_node = old_cur_node->next;
        }

        // 头部的random需要最后处理
        copied_nodes[head]->random = copied_nodes[head->random];

        return copied_nodes[head];
    }
};

int main(int argc, char *argv[])
{
    Areturn 0;
}
