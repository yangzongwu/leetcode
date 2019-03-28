using System;
public class Customer
{
    //classses,structs,enums,interfaces,delegates are called as types and 
    //fields,prooerties,constructions,methoeds ect.. that normally reside in a type are called type members
    #region Fields
    private int _id;
    private string _firstName;
    private string _lastName;
    #endregion;

    #region Properties
    public int Id
    {
        get { return _id; }
        set { _id = value; }
    }
    public string FirstName
    {
        get { return _firstName; }
        set { _firstName = value; }
    }
    public string LastName
    {
        get { return _lastName; }
        set { _lastName = value; }
    }
    #endregion

    #region Methods
    public string GetFullName()
    {
        return this._firstName + " " + this._lastName;
    }
    #endregion
}
public class Enums
{
    public static void Main()
    {
       
    }
}
