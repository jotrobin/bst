class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        rst, stack, pre = [], [], None
        
        while root or stack:
            
            while root:
                stack.append(root)
                root = root.left
                
            # for i in stack:
            #     print i.val,
            # print "\n"
            #check the top most node;
            if stack[-1].right and stack[-1].right != pre:
                root = stack[-1].right; continue
                
            pre = stack.pop()
            print "pre " + str(pre.val)
            rst.append(pre.val)
            
        return rst                      
