//
//  main.m
//  ZZHPROJECT
//
//  Created by 周子和 on 2021/2/23.
//

#import <UIKit/UIKit.h>
#import "ZZHAppDelegate.h"

int main(int argc, char * argv[]) {
    NSString * appDelegateClassName;
    @autoreleasepool {
        // Setup code that might create autoreleased objects goes here.
        appDelegateClassName = NSStringFromClass([ZZHAppDelegate class]);
    }
    return UIApplicationMain(argc, argv, nil, appDelegateClassName);
}
