/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.kleiver;

import java.util.Scanner;

/**
 *
 * @author Sala de Sistemas
 */
public class Kleiver {

    public static void main(String[] args) {
    
    
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite su nombre"); 
        String nombre = entrada.next();
        
        System.out.println("Digite su apellido ");
        String apellido = entrada.next();
        
        System.out.println("Digite su sexo Masculino(1)Femenino(2)");
        int sexo = entrada.nextInt();
        
        System.out.println("Edad su edad");
        int edad = entrada.nextInt();
        
        if (edad >=18){
            
            System.out.println("Eres legal"); }
            
            else {
                    System.out.println("No eres legal");
                    }
        
        if (sexo == 1){
            System.out.println("Eres hombre");
            
      
        }
        
        if (sexo == 2){
            System.out.println("Eres mujer");
        }
        
      
           
 }   
    }

